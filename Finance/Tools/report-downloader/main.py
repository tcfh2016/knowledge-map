import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
from datetime import datetime

# --- HKEX JSON scraping helpers -------------------------------------------

def _fetch_hkex_entries(range_days=7, lang='e', headers=None):
    """Return list of JSON entries from HKEXNews.

    HKEX’s public search UI is driven by a small JSON service that provides a
    rolling window of announcements.  Unfortunately the service only retains
    the last handful of days (1‑ or 7‑day ranges), so this helper can only
    fetch recent items.  For truly historical data you must use the web
    search page directly or run the script frequently and keep copies of
    downloaded reports.

    The relevant URL pattern looks like::

        https://www1.hkexnews.hk/ncms/json/eds/lcisehk{range}relsde_{page}.json

    ``range`` is either ``1`` (latest day) or ``7`` (last seven days) and the
    final ``e``/``c`` suffix denotes English/Chinese.  The function will
    iterate over pages until it reaches ``maxNumOfFile`` or encounters a
    non-200 response.
    """
    if headers is None:
        headers = {'User-Agent': 'Mozilla/5.0'}

    entries = []
    base = f'https://www1.hkexnews.hk/ncms/json/eds/lcisehk{range_days}relsde'
    page = 1
    while True:
        url = f"{base}_{page}.json"
        print(f"fetching {url}")
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            break
        data = resp.json()
        entries.extend(data.get('newsInfoLst', []))
        maxp = data.get('maxNumOfFile', 0)
        if page >= maxp:
            break
        page += 1
    return entries


def _filter_hkex_entries(entries, stock_codes=None, keywords=None):
    """Filter the raw json entries by stock code and/or keywords.

    ``stock_codes`` should be a list of strings such as ``['09626','01975']``.
    ``keywords`` are case insensitive substrings that must appear in the
    title/text/web path.  If both filters are provided they are applied using
    logical AND.
    """
    if stock_codes:
        stock_codes = set(stock_codes)
    if keywords:
        keywords = [k.lower() for k in keywords]

    out = []
    for e in entries:
        if stock_codes:
            codes = {st.get('sc') for st in e.get('stock', [])}
            if not (codes & stock_codes):
                continue
        if keywords:
            text = ' '.join(str(e.get(k, '')) for k in ('title', 'lTxt', 'sTxt', 'webPath'))
            text = text.lower()
            if not all(k in text for k in keywords):
                continue
        out.append(e)
    return out


def download_hkex_reports(stock_codes, output_dir="hkex_reports",
                           keywords=None, range_days=7, headers=None):
    """Download PDF documents matching criteria from HKEXNews.

    Parameters are self-explanatory; ``stock_codes`` is required (list of
    strings).  ``range_days`` may be 1 or 7; if you want older data you can
    run the script repeatedly on successive dates or loosen the keyword
    filtering.
    """
    if headers is None:
        headers = {'User-Agent': 'Mozilla/5.0'}

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    entries = _fetch_hkex_entries(range_days=range_days, headers=headers)
    print(f"fetched {len(entries)} total entries")
    selected = _filter_hkex_entries(entries, stock_codes, keywords)
    print(f"{len(selected)} entries match filters")

    downloaded = 0
    for e in selected:
        if e.get('ext','').lower() != 'pdf':
            continue
        href = e.get('webPath')
        if not href:
            continue
        fname = os.path.basename(href)
        filepath = os.path.join(output_dir, fname)
        if os.path.exists(filepath):
            print(f"skip existing {fname}")
            continue
        pdf_url = urljoin('https://www1.hkexnews.hk', href)
        print(f"downloading {fname} for stock {', '.join(st.get('sc','') for st in e.get('stock',[]))}")
        resp = requests.get(pdf_url, headers=headers, timeout=10)
        with open(filepath, 'wb') as f:
            f.write(resp.content)
        downloaded += 1
    print(f"done, {downloaded} files saved to {output_dir}")

def download_annual_reports(url, output_dir="annual_reports", 
                            keywords=None, headers=None):
    """
    Generic downloader that scans a page for PDF links containing one or more
    keywords in either the link text or URL.  Useful for grabbing annual reports
    from various investor‑relations sites.  

    Parameters
    ----------
    url : str
        The page to scrape.  Can be a full URL or the base of a site; relative
        hrefs will be joined against it.
    output_dir : str, optional
        Directory where downloaded PDFs will be stored (created if missing).
    keywords : list of str, optional
        List of case‑insensitive substrings to look for in the href or link
        text.  All keywords must be present.  By default the function will look
        for ``"annual"`` and ``"report"``.
    headers : dict, optional
        HTTP headers to supply with each request.  A minimal ``User-Agent`` is
        provided if none is given.
    """
    # default values
    if keywords is None:
        keywords = ["annual", "report"]
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        pdf_links = soup.find_all('a', href=True)

        downloaded_count = 0
        for link in pdf_links:
            href = link.get('href')
            text = link.get_text(" ")

            if not href or not href.lower().endswith('.pdf'):
                continue

            # check that every keyword is present in either href or link text
            lower_href = href.lower()
            lower_text = text.lower()
            if all(k.lower() in lower_href or k.lower() in lower_text for k in keywords):
                pdf_url = urljoin(url, href)
                filename = os.path.basename(href)
                filepath = os.path.join(output_dir, filename)

                if os.path.exists(filepath):
                    print(f"Skipping {filename}, already exists")
                    continue

                print(f"Downloading {filename}...")
                pdf_response = requests.get(pdf_url, headers=headers, timeout=10)
                with open(filepath, 'wb') as f:
                    f.write(pdf_response.content)
                print(f"✓ Saved: {filepath}")
                downloaded_count += 1

        print(f"\nDownload complete! {downloaded_count} file(s) downloaded.")

    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Download PDF files matching keywords from investor relations pages."
    )
    subparsers = parser.add_subparsers(dest="command")

    # generic URL scraper
    gp = subparsers.add_parser("url", help="scrape an arbitrary page for PDF links")
    gp.add_argument("-u", "--url", required=True,
                    help="URL of the page to scan")
    gp.add_argument("-o", "--output", default="downloads",
                    help="directory to save PDFs")
    gp.add_argument("-k", "--keywords", nargs='+', default=["annual", "report"],
                    help="keywords to match in link text or href")

    # HKEX-specific downloader
    hk = subparsers.add_parser("hkex", help="download annual reports from HKEXNews")
    hk.add_argument("-s", "--stocks", nargs='+', required=True,
                    help="stock code(s) to fetch (e.g. 09626)")
    hk.add_argument("-o", "--output", default="hkex_reports",
                    help="directory to save the downloaded PDFs")
    hk.add_argument("-k", "--keywords", nargs='+',
                    default=["annual", "report", "20-f"],
                    help="keywords to narrow the search results")
    hk.add_argument("-r", "--range", type=int, choices=[1,1000], default=7,
                    help="look-back range in days (1 or 1000)")

    args = parser.parse_args()
    if args.command == "hkex":
        print(f"HKEX download: stocks={args.stocks}, keywords={args.keywords}, range={args.range}d")
        download_hkex_reports(args.stocks, args.output,
                               keywords=args.keywords,
                               range_days=args.range)
    elif args.command == "url":
        print(f"scraping {args.url} for keywords {args.keywords}")
        download_annual_reports(args.url, args.output, keywords=args.keywords)
    else:
        parser.print_help()
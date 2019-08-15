# Web scraping

网页抓取，通过分析网页的组成形式来获取相应的内容。那些静态的，具有良好组织结构的网页通常
便于抓取抓取。

## Reading web page

从web 服务器抓取网页内容。

```
r = requests.get("https://www.baidu.com")
print(r.text[0:500])
```

## Parsing the HTML

使用 beautifulsoup4 来解析网页内容。

```
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs = {'class':'short-desc'})
print(results[0:3])
```

## Extracting the data

### Extract the line

```
first_result = results[0]

print(first_result.contents)
print(first_result.contents[1])
print(first_result.contents[1][1:-2])
```

### Extract the explanation

```
print(first_result.find('a'))
print(first_result.find('a').text[1:-1])
```

### Extract the URL

```
print(first_result.find('a'))
print(first_result.find('a')['href'])
```

## 参考

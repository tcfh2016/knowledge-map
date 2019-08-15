import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.douban.com/")
print(r.status_code)
#print(r.text[0:500])

soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs = {'class':'short-desc'})
#print(results[0:3])

first_result = results[0]
print(first_result)
print(first_result.find('strong'))
print(first_result.find('strong').text)
print(first_result.find('strong').text[0, -1])
print(first_result.find('strong').text[0, -1] + ', 2017')

print(first_result.contents)
print(first_result.contents[1])
print(first_result.contents[1][1:-2])

# 引出explanation
print(first_result.contents[2])
print(first_result.find('a'))
print(first_result.find('a').text[1:-1])

# 引出超链接
print(first_result.find('a'))
print(first_result.find('a')['href'])

records = []
for result in results:
    date = result.find('strong').text[0,-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))

import pandas as pd
df = pd.DataFrame(records, columns=['data', 'lie', 'explanation', 'url'])
printf(df.head())
printf(df.tail())
df['date'] = pd.to_datetime(df['date'])
printf(df.head())

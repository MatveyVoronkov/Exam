import requests
from bs4 import BeautifulSoup as bs


grn = int(input('Enter grn: '))
r = requests.get("https://privatbank.ua/rates-archive")
html = bs(r.text, "html.parser")
data = html.find_all('div', class_='purchase')
cur = []
for i in data:
    cur.append(float(i.span.text))
print('Your ammount in 'f'USD = {grn / cur[1]}')
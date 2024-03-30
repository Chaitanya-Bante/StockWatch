import requests
from bs4 import BeautifulSoup as bs

url = "https://www.google.com/finance/?hl=en"

response = requests.get(url)

soup = bs(response.text, 'html.parser')

stocks = soup.find_all('a', {'class':'NaLFgc'})

stock_names = []
stock_change = []

for stock in stocks:
    stock_names = soup.find_all('div', {'class':'TwnKPb'})
    stock_change = soup.find_all('div', {'class':'JwB6zf'})
    
for i in range(len(stocks)):
        print(stock_names[i].string + ' ' + str(stock_change[i].string))
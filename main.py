import requests
from bs4 import BeautifulSoup as bs

url = "https://www.google.com/finance/?hl=en"

response = requests.get(url)

soup = bs(response.text, 'html.parser')

links = soup.find_all('a')

for link in links:
    print(link.get('href'))
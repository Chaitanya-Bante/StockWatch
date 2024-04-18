from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)

@app.route('/')
def Welcome():
    url = "https://www.moneycontrol.com/markets/indian-indices/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = soup.find_all('table', {'class':'tbl_indices'})

    stock_info = []

    for tables in data[0:5]:
        rows = tables.find_all('tr')
        for row in rows:
            tds = row.find_all('td')
            if len(tds) <= 1:
                continue
            else:
                Name = tds[0].string
                Price = tds[2].string
                Change = tds[3].string
                percentChange = tds[4].string
                
                if float(percentChange) < 0.0:
                    color = 'redText'
                else:
                    color = 'greenText'

                stock_info.append([Name, Price, Change, percentChange, color])

    # random.shuffle(stock_info)

    return render_template('index.html', stock_info = sorted(stock_info))



if __name__ == '__main__':
    app.run(debug=True)
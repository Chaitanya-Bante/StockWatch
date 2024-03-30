from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup as bs
import requests

app = Flask(__name__)

@app.route('/')
def Welcome():
    url = "https://www.google.com/finance/?hl=en"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    stock_names_div = soup.find_all('div', {'class':'TwnKPb'})
    stock_change_div = soup.find_all('div', {'class':'JwB6zf'})

    stock_names = []
    stock_change = []

    for i in range(len(stock_names_div)):
        stock_names.append(stock_names_div[i].string)
        stock_change.append(stock_change_div[i].string)

    stock_info = merge_lists(stock_names, stock_change)
    
    return render_template('index.html', stock_info = stock_info)

def merge_lists(list1, list2):
        merged_list = []
        min_length = min(len(list1), len(list2))
        for i in range(min_length):
            merged_list.append([list1[i], list2[i]])
        return merged_list

if __name__ == '__main__':
    app.run(debug=True)
# -*- coding: utf-8 -*-
from flask import Flask, request # Flaskパッケージをインポート
import requests
# from bs4 import BeautifulSoup

app = Flask(__name__) # Flaskクラスのインスタンス生成

@app.route('/', defaults={'path': ''}) # URLを指定。URLにリクエストが来ると関数が実行される
def index():
    """
    html = res.text
    sorp = BeautifulSoup(html, 'html.parser')
    title = sorp.find('title')
    return title.text
    """
    res = requests.get('https://api.github.com/users/taiga-tech')
    return res.json()

@app.route('/search')
def analyzer():
    query = ""
    if request.args.get('q') is not None:
        query = request.args.get('q')
    else:
        query = "パラメーターがないよ"
    return query

@app.route('/favicon.ico')
def favicon():
    return ""

if __name__ == '__main__':
	app.run(debug=True)

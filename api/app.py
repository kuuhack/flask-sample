# -*- coding: utf-8 -*-
# Flaskパッケージをインポート
from flask import Flask, request , Response
import requests
# from bs4 import BeautifulSoup
# from .gh import ghu

# Flaskクラスのインスタンス生成
app = Flask(__name__)

# URLを指定。URLにリクエストが来ると関数が実行される
@app.route('/<username>')
def index(username: str):
    '''
    html = res.text
    sorp = BeautifulSoup(html, 'html.parser')
    title = sorp.find('title')
    return title.text
    '''
    res = requests.get(f'https://api.github.com/users/{username}')
    return res.json()

@app.route('/search')
def analyzer():
    query = ''
    if request.args.get('q') is not None:
        query = request.args.get('q')
    else:
        query = 'パラメーターがない'
    return Response(query, mimetype='text/plain')

@app.route('/favicon.ico')
def favicon():
    return ''

if __name__ == '__main__':
	app.run()

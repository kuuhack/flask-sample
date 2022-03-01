# -*- coding: utf-8 -*-
# Flaskパッケージをインポート
from flask import Flask, render_template
import requests
# import controllers
# from controllers import gh, search, favicon

# Flaskクラスのインスタンス生成
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<username>')
def ghu(username: str):
    '''
    html = res.text
    sorp = BeautifulSoup(html, 'html.parser')
    title = sorp.find('title')
    return title.text
    '''
    res = requests.get(f'https://api.github.com/users/{username}')
    return res.json()

# # /api/vi/<username>
# app.register_blueprint(gh.app)
# # /api/v1/search?q=<query>
# app.register_blueprint(search.app)

# app.register_blueprint(favicon.app)

if __name__ == '__main__':
	app.run()

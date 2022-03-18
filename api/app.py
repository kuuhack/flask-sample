# -*- coding: utf-8 -*-
# Flaskパッケージをインポート
from flask import Flask, render_template
# import controllers
from .controllers import favicon, gh, search

# Flaskクラスのインスタンス生成
app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# /api/vi/<username>
app.register_blueprint(gh.app)
# /api/v1/search?q=<query>
app.register_blueprint(search.app)

app.register_blueprint(favicon.app)

if __name__ == '__main__':
	app.run()

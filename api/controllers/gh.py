from flask import Blueprint
import requests
# from bs4 import BeautifulSoup

app = Blueprint('gh', __name__, url_prefix='/api/v1')

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

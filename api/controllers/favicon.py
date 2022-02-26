from flask import Blueprint

app = Blueprint('favicon', __name__)

@app.route('/favicon.ico')
def favicon():
    return ''

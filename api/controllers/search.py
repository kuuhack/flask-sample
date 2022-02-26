from flask import Blueprint, Response, request

app = Blueprint('search', __name__, url_prefix='/api/v1')

@app.route('/search')
def analyzer():
    query = ''
    if request.args.get('q') is not None:
        query = request.args.get('q')
    else:
        query = 'パラメーターがない'
    return Response(query, mimetype='text/plain')

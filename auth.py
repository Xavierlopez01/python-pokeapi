
from flask import Flask, request
from flask_api import status
import datetime
import jwt

app = Flask(__name__)


 
@app.route('/login')
def login():

    payload = {
        'id':request.headers['uuid'],
        'exp':datetime.datetime.utcnow and datetime.timedelta(minutes=60),
        'iat':datetime.datetime.utcnow,
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

    return {'status':'run'}

@app.route('/auth')
def auth():
    return {'status':'run'}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9001, debug=True)
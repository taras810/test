from app import app
from flask import render_template, request, jsonify
import requests
import os


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/add_message', methods=['POST'])
def add_message():
    card = request.form['card']
    cvv = request.form['cvv']
    exp = request.form['exp']
    #INBOUND
    res = requests.post("https://tntj8irdonu.sandbox.verygoodproxy.com/post",
                            json={'card': card, 'cvv': cvv, 'exp': exp})

    card = res.json()['json']['card']
    cvv = res.json()['json']['cvv']
    exp = res.json()['json']['exp']
    return render_template('message.html', card=card, cvv=cvv, exp=exp)


@app.route("/forward", methods=['POST'])
def forward():
    card = request.form['card']
    cvv = request.form['cvv']
    exp = request.form['exp']
    #OUTBOUND
    os.environ['HTTPS_PROXY'] = 'https://USpx24YqzCvYjzxDwc1mDU9K:779c56a9-4b14-459e-9fd8-d11cc45052cc@tntj8irdonu.sandbox.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                        json={'card': card, 'cvv': cvv, 'exp': exp},
                        verify='cert.pem')

    card = res.json()['json']['card']
    cvv = res.json()['json']['cvv']
    exp = res.json()['json']['exp']
    return render_template('forward.html', card=card, cvv=cvv, exp=exp)
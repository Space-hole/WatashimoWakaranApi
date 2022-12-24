from flask import Flask
from DB import SignUp, msg, createChan, createServer
import random

app = Flask(__name__)

from flask import jsonify

@app.route("/")
def home():
    return "HELLOOO"

@app.route('/msg/<id>/<name>/<text>/')
def msgs(id, name, text):
    msg(id, text, text)
    return jsonify({"id": id,
                    "name": name,
                    "text": text}), 200

@app.route('/signup/<id>/<name>/<passw>/')
def signu(id, name, passw):
    SignUp(id, name, passw)
    return jsonify({"id": id,
                    "name": name,
                    "pass": passw}), 200

@app.route('/create/<id>/<name>/')
def createSv(id, name):
    createServer(id, name)
    return jsonify({"id": id,
                    "name": name}), 200

@app.route('/channel/<id>/<name>/')
def createCha(id, name):
    createChan(id, name)
    return jsonify({"id": id,
                    "name": name}), 200

app.run(
    host='0.0.0.0',
	port=random.randint(2000,9000)
)

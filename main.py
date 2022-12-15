from flask import Flask
from DB import *

app = Flask(__name__)

from flask import jsonify

@app.route('/msg/<id>/<name>/<text>/')
def msgs(id, name, text):
    msg("Msgs", text, id)
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
def createChan(id, name):
    createServer(id, name)
    return jsonify({"id": id,
                    "name": name}), 200

app.run()

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

app.run()

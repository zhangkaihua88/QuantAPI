from flask import Flask, request
import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from tqdm import tqdm
import copy
import requests
import base64   
from time import sleep


ALL_SESS = {}
BASE_AUTH = ''

app = Flask(__name__)

def wait_get(sess, url):
    while True:
        response = sess.get(url)
        if response.headers.get("Retry-After", 0) == 0:
            break
        sleep(float(response.headers["Retry-After"]))
    return response



@app.route('/authentication', methods=['GET'])
def login():
    Authorization = request.headers.get('Authorization', BASE_AUTH)
    Authorization = Authorization.split(' ')[-1]

    decoded_bytes = base64.b64decode(Authorization)
    decoded_string = decoded_bytes.decode('utf-8')
    username, password = decoded_string.split(':')
    sess = requests.Session()
    sess.auth = (username, password)
    response = sess.post('https://api.worldquantbrain.com/authentication')
    ALL_SESS[Authorization] = sess
    return response.text

@app.route('/<path:path>', methods=['GET'])
def redirect_to_other(path):
    Authorization = request.headers.get('Authorization', BASE_AUTH)
    Authorization = Authorization.split(' ')[-1]
    response = wait_get(ALL_SESS[Authorization], f"https://api.worldquantbrain.com/{path}")
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

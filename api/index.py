from flask import Flask, request
import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from tqdm import tqdm
import copy
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'




@app.route('/authentication', methods=['GET'])
def login():
    headers = request.headers
    # username = "***REMOVED***"
    # password = "***REMOVED***"

    # s = requests.Session()
    # s.auth = (username, password)
    # response = s.post('https://api.worldquantbrain.com/authentication')
    # print(response)
    return type(headers)

# @app.route('/<path:path>', methods=['GET', 'POST'])
# def redirect_to_other(path):
#     # 这里将所有除登录外的请求重定向到其他网站
#     return redirect(f'https://otherwebsite.com/{path}')

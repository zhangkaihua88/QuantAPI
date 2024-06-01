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
    headers_keys = dict(request.headers)
    
    # 转换为列表（方便查看或其他操作）
    # headers_list = list(headers_keys)
    
    return f"{headers_keys}"
    # headers = request.headers.keys()
    # username = "***REMOVED***"
    # password = "***REMOVED***"

    # s = requests.Session()
    # s.auth = (username, password)
    # response = s.post('https://api.worldquantbrain.com/authentication')
    # print(response)
    # return type(headers)
    # user_agent = request.headers.get('User-Agent')
    
    # Alternatively, you can use dictionary-like access
    # host = request.headers['Host']

    # return f"User-Agent: {user_agent}, Host: {host}"

# @app.route('/<path:path>', methods=['GET', 'POST'])
# def redirect_to_other(path):
#     # 这里将所有除登录外的请求重定向到其他网站
#     return redirect(f'https://otherwebsite.com/{path}')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

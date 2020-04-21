from flask import Flask, request

import execjs
import requests

app = Flask(__name__)

@app.route('/question', methods=["POST"])
def question():
    if request.method == "POST":
        question = request.form['question']

        js = execjs.compile('''
            function encrypt(title){
                var CryptoJS = require('./myjs');
    
                var key = '39383033327777772e313530732e636e';
                key = CryptoJS.enc.Hex.parse(key);
                var enc = CryptoJS.AES.encrypt(title ,key);
                var enced = enc.ciphertext.toString();

                return enced;
            };
        ''')

        url = "https://www.150s.cn/topic/getSubject"
        headers = {"Content-Type":"application/x-www-form-urlencoded", "Accept-Language":"zh-CN,en-US;q=0.8,en;q=0.6,zh;q=0.4"}
        data = {"secret":js.call('encrypt', question), "title":question}
        cookies = dict(JSESSIONID='13C7A0FC413FF43A4E98715E4D9DF78F', UM_distinctid='17196b5b0502ae-081894d8c1190a-325e2766-59b90-17196b5b051203', CNZZDATA1278612510='642624008-1587371003-%7C1587371003', Hm_lvt_b656d8b02edc9a9cf671edf4ceeddbc3='1587371423', Hm_lpvt_b656d8b02edc9a9cf671edf4ceeddbc3='1587371423')

        resp = requests.post(url = url, headers = headers, data = data, cookies = cookies, timeout = 1)

        return resp.text

from app import views
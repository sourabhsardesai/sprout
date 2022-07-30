#!/usr/bin/env python
# encoding: utf-8
import http
import json
from flask import Flask , request , jsonify
from services import ml_service
DB = []
app = Flask(__name__)
@app.route('/')
def index():

    return json.dumps(ml_service.get_all())

@app.route('/sentences', methods = ['POST'])
def ml_service_caller():
    print(request.data)
    respone = json.loads(request.data)
    final_res = ml_service.detect_senti(respone)
    return final_res

@app.route('/posts', methods = ['POST'])
def posts():
    #print(request.data)
    response = json.loads(request.data)
    final_res = ml_service.foul_lang(response)
    return final_res



app.run()
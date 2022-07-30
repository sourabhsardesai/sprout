
#Initializing of the project, this file contains all the api declarations
#!/usr/bin/env python
# encoding: utf-8
import http
import json
from flask import Flask , request , jsonify
from services import ml_service
DB = []
app = Flask(__name__)
# This api gets all the data records stored in the DB/list
@app.route('/')
def index():
    try:
        return json.dumps(ml_service.get_all())
    except:
        return json.dumps({"response":"something went wrong"})
# This is the internal api which accepts a single sentence and returns the foul sentiment as the response.
@app.route('/sentences', methods = ['POST'])
def ml_service_caller():
    try:
        print(request.data)
        respone = json.loads(request.data)
        final_res = ml_service.detect_senti(respone)
        return final_res
    except:
        return json.dumps({"response": "something went wrong"})
# This api accepts the posts and calls an internal api within to give sentiment to the user
@app.route('/posts', methods = ['POST'])
def posts():
    #print(request.data)
    try:
        response = json.loads(request.data)
        final_res = ml_service.foul_lang(response)
        return final_res
    except:
        return json.dumps({"response":"something went wrong"})



app.run()
import json

from flask import jsonify
import requests
import random
DB = []
internal_api = 'http://127.0.0.1:5000/sentences'



def get_all():
    return(json.dumps(DB))

def detect_senti(respone):
    print("record")
    record = {
        "sentence":respone,
        "hasFoulLanguage":bool(random.getrandbits(1))
    }
    print(record)


    return record

def foul_lang(response):

    print(response['paragraph'])
    for par in response['paragraph']:
        print(par)
        record = {
            "fragment":str(par)
                    }
        print(json.dumps(record))
        r = requests.post(url=internal_api, data= json.dumps(record))
        print("result of algo = ",r.json())
        DB.append(r.json())



    return(json.dumps(DB))

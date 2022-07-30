# This file has all the functions related to the apis
import json

from flask import jsonify
import requests
import random
DB = [] # Db /list
internal_api = 'http://127.0.0.1:5000/sentences' # internal api


# This functions gets all the records in the DB/ list
def get_all():
    return(json.dumps(DB))

# function which detects the sentiment
def detect_senti(respone):
    print("record")
    record = {
        "sentence":respone,
        "hasFoulLanguage":bool(random.getrandbits(1))
    }
    print(record)


    return record
# function which seperates the sentences from a para and calls an internal api
def foul_lang(response):

    print(response['paragraphs'])
    for par in response['paragraphs']:
        print(par)
        record = {
            "fragment":str(par)
                    }
        print(json.dumps(record))
        r = requests.post(url=internal_api, data= json.dumps(record))
        print("result of algo = ",r.json())
        DB.append(r.json())



    return(json.dumps(DB))

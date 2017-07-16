import json
import os
import requests


def get_definition(word):
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/definitions"
    api_key = str(os.environ.get("Mashape-key"))
    header = {
        "X-Mashape-Key": api_key,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=header)
    print json.dumps(response.json())
    json_response = json.loads(response.text)
    # type_list = json_response['definitions'][0]['partOfSpeech']
    # print type_list
    for index, type in enumerate(json_response, start=0):
        print index
        print type
        type_list = json_response['definitions'][index]['partOfSpeech']
        print type_list


get_definition("example")

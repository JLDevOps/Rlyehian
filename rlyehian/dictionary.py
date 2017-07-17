import csv
import json
import os
import requests


def api_call_definitions(word):
    url = "https://wordsapiv1.p.mashape.com/words/" + word + "/definitions"
    api_key = str(os.environ.get("Mashape-key"))
    header = {
        "X-Mashape-Key": api_key,
        "Accept": "application/json"
    }
    response = requests.get(url, headers=header)
    json_response = json.loads(response.text)
    return json_response


def get_partOfSpeech(json_definition):
    type_list = []
    try:
        for index, item in enumerate(json_definition['definitions']):
            word_type = json_definition['definitions'][index]['partOfSpeech']
            if word_type not in type_list:
                type_list.append(word_type)
        return type_list
    except Exception:
        return


def get_definition(json_definition):
    type_list = []
    try:
        for index, item in enumerate(json_definition['definitions']):
            word_type = json_definition['definitions'][index]['definition']
            if word_type not in type_list:
                type_list.append(word_type)
        return type_list
    except Exception:
        return


def check_csv_header(path, file_name):
    os.chdir(path)
    file_path = os.path.join(path, file_name)
    with open(file_path, "rb") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        if (header == None):
            with open(file_path, "a") as file:
                file.writelines("Word,Primary Type,Secondary Type\n")


def append_csv(path, file_name, word_information):
    os.chdir(path)
    file_path = os.path.join(path, file_name)
    with open(file_path, 'a') as file:
        file.writelines(word_information + "\n")


def read_csv(path, file_name):
    os.chdir(path)
    file_path = os.path.join(path, file_name)
    with open(file_path, "rb") as file:
        reader = csv.DictReader(file)
        data = {}
        for row in reader:
            for header, value in row.items():
                try:
                    data[header].append(value)
                except KeyError:
                    data[header] = [value]
        return data


def append_data(word, type_list):
    try:
        type_data = ",".join(map(str, type_list))
        word_row = str(word) + "," + type_data + ","
        return word_row
    except Exception:
        return str(word) + ",,"


def create_word_file(path, read_file, write_file):
    data = read_csv(path, read_file)
    try:
        word_column = data['Word']
    except Exception:
        word_column = data['word']
    check_csv_header(path, write_file)

    for index, item in enumerate(word_column):
        response = api_call_definitions(word_column[index])
        word = get_partOfSpeech(response)
        result = append_data(word_column[index], word)
        append_csv(path, write_file, result)

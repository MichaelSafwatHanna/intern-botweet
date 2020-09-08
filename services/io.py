import json
import os
from os.path import join

resources_path = join(os.getcwd(), 'resources/')
app_settings = join(resources_path, 'app-cache.json')

import services.config as config


def read_cache():
    file = open(config.app_cache_path, "r")
    file_json = json.load(file)
    file.close()
    return file_json


def write_cache(resources):
    file = open(config.app_cache_path, "w")
    file.write(json.dumps(resources, indent=2))
    file.close()


def add_text_to_file(text, append):
    file_json = read_cache()
    if append:
        file_json['text'] = file_json['text'] + ". " + text
    else:
        file_json['text'] = text

    write_cache(file_json)


def load_text():
    file_json = read_cache()
    text = file_json['text']
    return text

import json
import os
from os.path import join

resources_path = join(os.getcwd(),
                      'resources/tone-document.json')


def add_new_text_to_file(text):
    file = open(resources_path, "w")
    json_text = {
        "text": text
    }
    file.write(json.dumps(json_text, indent=2))
    file.close()


def append_text_to_file(text):
    file = open(resources_path, "r")
    old_text = json.load(file)['text']
    file.close()

    json_text = {
        "text": old_text + ", " + text
    }
    
    file = open(resources_path, "w")
    file.write(json.dumps(json_text, indent=2))
    file.close()

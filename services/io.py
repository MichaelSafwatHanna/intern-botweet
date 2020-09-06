import json
import os
from os.path import join

resources_path = join(os.getcwd(),
                      'resources/tone-document.json')


def add_text_to_file(text, append):
    file = open(resources_path, "r")
    old_file = json.load(file)
    file.close()
    if append:
        old_file['text'] = old_file['text'] + ", " + text
    else:
        old_file['text'] = text

    file = open(resources_path, "w")
    file.write(json.dumps(old_file, indent=2))
    file.close()


def load_text():
    file = open(resources_path, "r")
    text = json.load(file)['text']
    file.close()
    return text

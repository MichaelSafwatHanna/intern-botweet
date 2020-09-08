import datetime
import json

from dateutil.parser import parse as datetime_parser

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


def reset_tweets_index(file_json):
    file_json['index'] = 0


def validate_cached_data():
    file_json = read_cache()
    cached_date = datetime_parser(file_json['date']).date()
    if cached_date != datetime.date.today():
        file_json['date'] = str(datetime.date.today())
        reset_tweets_index(file_json)

    write_cache(file_json)

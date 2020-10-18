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


def set_tweets_index(file_json, index):
    file_json['index'] = index


def increment_tweets_index(file_json):
    file_json['index'] += 1


def reset_tweets_index(file_json):
    file_json['index'] = 0


def update_last_tweet_id(last_id, index):
    file_json = read_cache()
    file_json['last_id'] = last_id
    if index:
        set_tweets_index(file_json, index)
    else:
        increment_tweets_index(file_json)
    write_cache(file_json)


def validate_cached_data():
    file_json = read_cache()
    cached_date = datetime_parser(file_json['date']).date()
    if cached_date != datetime.date.today():
        file_json['date'] = str(datetime.date.today())
        reset_tweets_index(file_json)

    write_cache(file_json)

import json
import os
from os.path import join

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ToneAnalyzerV3

API_KEY = 'API KEY'
SERVICE_URL = 'SERVICE_URL'

authenticator = IAMAuthenticator(API_KEY)
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)
tone_analyzer.set_service_url(SERVICE_URL)


def analyze_document():
    with open(join(os.getcwd(),
                   'resources/tone-document.json')) as text:
        tone = tone_analyzer.tone(
            json.load(text)['text'],
            content_type='text/html').get_result()
    return tone['document_tone']

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ToneAnalyzerV3

API_KEY = 'API_KEY'
SERVICE_URL = 'SERVICE_URL'

authenticator = IAMAuthenticator(API_KEY)
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)
tone_analyzer.set_service_url(SERVICE_URL)


def analyze(text):
    tone = tone_analyzer.tone(
        tone_input=text,
        content_type="text/plain").get_result()
    return tone['document_tone']

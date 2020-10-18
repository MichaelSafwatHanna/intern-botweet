import twitter

CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'
ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'

CHARACTER_LIMIT = 280

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)



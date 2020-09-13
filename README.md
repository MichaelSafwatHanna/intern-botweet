# :technologist: intern-botweet

I started a thread on my twitter account on my first day as a 3-month backend intern and decided to tweet about my everyday impression, so I thought I may build a custom twitter CLI client, that analyzes the tone of my tweet to tag each day with a numbered impression and then post it on behalf of me.

## Used services

1. [IBM Watson's API](https://github.com/watson-developer-cloud/python-sdk)

2. [Twitter API](https://python-twitter.readthedocs.io/en/latest/index.html)

## Getting Started :hourglass:

- [Getting started with IBM Watson API](https://github.com/watson-developer-cloud/python-sdk#authentication)

  - Get your keys and add them to `services/tone_analyzer.py`

    ```python
    API_KEY = 'API_KEY'
    SERVICE_URL = 'SERVICE_URL'
    ```

- [Getting started with Twitter API](https://python-twitter.readthedocs.io/en/latest/getting_started.html)

  - Create a [Twitter App](https://apps.twitter.com/). Click the “Create New App” button and fill out the fields on the next page.
  - Once your app is created, you’ll be directed to a new page showing you some information about it.
  - Click on the `Keys and Access Tokens` tab on the top there.
  - At this point, you can add the keys which are under `Your Application Tokens` to test out your application, specifically at `services/twitter.py`.

    ```python
    consumer_key = 'consumer_key'
    consumer_secret = 'consumer_secret'
    access_token = 'access_token'
    access_token_secret = 'access_token_secret'
    ```

## Commands

### Test

- Synopsis

```bash
test [OPTIONS] [TWEET TEXT]
```

- Description

  - Logs the tweet with tone analysis if `stats option` is included.

- Options
  - `-s, --stats`
    Analyze tone of the tweet text and include it in the tweet.

### Tweet

- Synopsis

```bash
tweet [OPTIONS] [TWEET TEXT]
```

- Description

  - Post the tweet with tone analysis if `stats option` is included.

- Options
  - `-s, --stats`
    Analyze tone of the tweet text and include it in the tweet.
  - `-y`
    Bypasses the post tweet prompt.

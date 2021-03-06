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
    CONSUMER_KEY = 'CONSUMER_KEY'
    CONSUMER_SECRET = 'CONSUMER_SECRET'
    ACCESS_TOKEN = 'ACCESS_TOKEN'
    ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'
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
  - `-t`
    Post the tweet without prompt.
  - `-v, --verbose`
    Logs metadata of the tweet after posting.

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
    Post the tweet without prompt.
  - `-v, --verbose`
    Logs metadata of the tweet after posting.

### slti

- Synopsis

```bash
slti [TWEET ID]
```

- Description

  - Sets the last tweet id in the persistent cache.

### rd

- Synopsis

```bash
rd
```

- Description

  - Prints remaining days and business days.

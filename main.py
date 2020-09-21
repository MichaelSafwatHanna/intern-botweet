import getopt
import io
import sys

import services.twitter as twitter
from models.tweet import Tweet
from services import io as io_service
from services import tone_analyzer
from services.logger import Logger, Color

options = "sytv"
long_options = ["stats", "verbose"]
command = sys.argv[1]
logger = Logger()

# activate logger colors
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')


def main(args):
    io_service.validate_cached_data()
    try:
        opts, args = getopt.getopt(args, options, long_options)
        if command == "test":
            test_command(opts, args)
        elif command == "tweet":
            tweet_command(opts, args)
    except getopt.GetoptError:
        pass


def log_tweet(tweet):
    logger.color = Color.Cyan
    logger.log(tweet)
    logger.color = Color.Yellow
    logger.log("[Characters count]: " + str(len(tweet)))
    validate_char_limit(tweet)


def validate_char_limit(tweet):
    if len(tweet) > twitter.CHARACTER_LIMIT:
        logger.color = Color.Red
        logger.log("Tweet characters exceed the limit!")
        exit(1)


def test_command(opts, args):
    t_flag = False
    v_flag = False
    cache = io_service.read_cache()
    text = ' '.join(args)
    tweet = Tweet(cache['index'], text, None, cache['last_id'])

    for opt, arg in opts:
        if opt in ("-s", "--stats"):
            tweet.tone_analysis = tone_analyzer.analyze(text)
        if opt == "-t":
            t_flag = True
            if opt in ("-v", "--verbose"):
                v_flag = True

    tweet_str = tweet.to_string()
    log_tweet(tweet_str)

    if t_flag:
        push_tweet(tweet_str, tweet.in_reply_to_id, v_flag)


def tweet_command(opts, args):
    y_flag = False
    v_flag = False
    cache = io_service.read_cache()
    text = ' '.join(args)
    tweet = Tweet(cache['index'], text, None, cache['last_id'])

    for opt, arg in opts:
        if opt == "-y":
            y_flag = True
        if opt in ("-s", "--stats"):
            tweet.tone_analysis = tone_analyzer.analyze(text)
        if opt in ("-v", "--verbose"):
            v_flag = True

    tweet_str = tweet.to_string()
    log_tweet(tweet_str)

    if not y_flag:
        logger.color = Color.Red
        logger.log("Do you want to tweet? (y/n)")
        choice = input()
        if choice != "y" and choice != "Y":
            return

    push_tweet(tweet_str, tweet.in_reply_to_id, v_flag)


def push_tweet(tweet, in_reply_to_id, verbose_flag):
    twitter_tweet = twitter.api.PostUpdate(tweet, in_reply_to_status_id=in_reply_to_id)
    io_service.update_last_tweet_id(twitter_tweet.id)
    logger.color = Color.Green
    logger.log("Tweet Posted Successfully!")
    if verbose_flag:
        logger.color = Color.Green
        logger.log(f"Created at: [{twitter_tweet.created_at}]")
        logger.log(f"Tweet id: [{twitter_tweet.id}]")
        logger.log(f"In reply to status id: [{twitter_tweet.in_reply_to_status_id}]")


if __name__ == "__main__":
    main(sys.argv[2:])

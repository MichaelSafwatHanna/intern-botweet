import getopt
import io
import sys

import services.twitter as twitter
from models.tweet import Tweet
from services import io as io_service
from services import tone_analyzer
from services.logger import Logger, Color

options = "sy"
long_options = ["stats"]
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
    logger.color = Color.Orange
    logger.log("Characters: " + str(len(tweet)))


def test_command(opts, args):
    stats = None
    text = ' '.join(args)
    tweet = None
    tweet_str = None
    for opt, arg in opts:
        if opt in ("-s", "--stats"):
            stats = tone_analyzer.analyze(text)
            cache = io_service.read_cache()
            tweet = Tweet(cache['index'], text, stats, cache['last_id'])
            tweet_str = tweet.to_string()
            log_tweet(tweet_str)

            logger.color = Color.Red
            logger.log("Do you want to tweet? (y/n)")
            choice = input()
            if choice == "y" or choice == "Y":
                push_tweet(tweet_str, tweet.in_reply_to_id)


def tweet_command(opts, args):
    y_flag = False
    stats = None
    text = ' '.join(args)
    tweet = None
    tweet_str = None
    for opt, arg in opts:
        if opt == "-y":
            y_flag = True
        if opt in ("-s", "--stats"):
            stats = tone_analyzer.analyze(text)
            cache = io_service.read_cache()
            tweet = Tweet(cache['index'], text, stats, cache['last_id'])
            tweet_str = tweet.to_string()
            log_tweet(tweet_str)

    if not y_flag:
        logger.color = Color.Red
        logger.log("Do you want to tweet? (y/n)")
        choice = input()
        if choice != "y" and choice != "Y":
            return

    push_tweet(tweet_str, tweet.in_reply_to_id)


def push_tweet(tweet, in_reply_to_id):
    twitter_tweet = twitter.api.PostUpdate(tweet, in_reply_to_status_id=in_reply_to_id)
    io_service.update_last_tweet_id(twitter_tweet.id)
    logger.color = Color.Green
    logger.log("Tweet Posted Successfully!")


if __name__ == "__main__":
    main(sys.argv[2:])

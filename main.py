import datetime
import getopt
import io
import sys

from models.tweet import Tweet
from services import io as io_service
from services import tone_analyzer
from services.logger import Logger, Color

options = "s"
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

    except getopt.GetoptError:
        pass


def log_tweet(tweet):
    logger.color = Color.Cyan
    logger.log(tweet)
    logger.color = Color.Red
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


if __name__ == "__main__":
    main(sys.argv[2:])

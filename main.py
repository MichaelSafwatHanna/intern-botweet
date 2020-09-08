import datetime
import getopt
import io
import sys

from models.tweet import Tweet
from services import io as io_service
from services import tone_analyzer
from services.config import day_zero
from services.logger import Logger, Color

options = "n:a:s"
long_options = ["new=", "append=", "stats"]
command = sys.argv[1]
stats_flag = sys.argv.__contains__("--stats") or sys.argv.__contains__("-s")
logger = Logger()
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')


def main(args):
    io_service.validate_cached_data()
    opts, args = getopt.getopt(args, options, long_options)

    if command == "add":
        add_command(opts)

    if stats_flag:
        stats = tone_analyzer.analyze_document()
        cache = io_service.read_cache()
        day_n = (datetime.date.today() - day_zero).days
        tweet = Tweet(day_n, cache['index'], cache['text'], stats)
        tweet_str = tweet.to_string()

        logger.color = Color.Cyan
        logger.log(tweet_str)

        logger.color = Color.Red
        logger.log("Characters: " + str(len(tweet_str)))


def add_command(opts):
    for opt, arg in opts:
        if opt in ("-a", "--append"):
            io_service.add_text_to_file(arg, append=True)
            break
        elif opt in ("-n", "--new"):
            io_service.add_text_to_file(arg, append=False)
            break


if __name__ == "__main__":
    main(sys.argv[2:])

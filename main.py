import getopt
import sys

from services import tone_analyzer, io

options = "n:a:"
long_options = ["new=", "append="]
command = sys.argv[1]


def main(args):
    opts, args = getopt.getopt(args, options, long_options)

    if command == "add":
        add_command(opts)


def add_command(opts):
    for opt, arg in opts:
        if opt in ("-a", "--append"):
            io.add_text_to_file(arg, append=True)
            break
        elif opt in ("-n", "--new"):
            io.add_text_to_file(arg, append=False)
            break


if __name__ == "__main__":
    main(sys.argv[2:])

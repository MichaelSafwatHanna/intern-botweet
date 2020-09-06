import getopt
import sys

import io_service

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
            io_service.append_text_to_file(arg)
            break
        elif opt in ("-n", "--new"):
            io_service.add_new_text_to_file(arg)
            break


if __name__ == "__main__":
    main(sys.argv[2:])

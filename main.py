"""Some documentation."""
import argparse
import sys


def reverse_and_upper(string):
    """Return uppercased and reversed string."""
    return ''.join(reversed(string.upper()))


def parse_args(args):
    """So I can nicly Pytesting."""
    ap_reworked = argparse.ArgumentParser()
    ap_reworked.add_argument("-s", "--string", required=True, help="Please "
                             "enter, string you would like to uppercase"
                             " andreverse ")
    return ap_reworked.parse_args(args)


if __name__ == "__main__":
    ARGS_MAIN = parse_args(sys.argv[1:])
    print(reverse_and_upper(ARGS_MAIN.string))

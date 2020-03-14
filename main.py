import argparse

def reverse_and_upper():
    """
    :return:
    is returning uppercased  and reversed string
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--string", required=True, help="Please enter, string you would like to uppercase and reverse ")
    args = vars(ap.parse_args())
    string = args["string"]
    return (''.join(reversed(string.upper())))


if __name__ == "__main__":
    print(reverse_and_upper())
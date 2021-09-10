import argparse
import src.parser as parser

def main():
    opt = parse_args()
    p = parser.Parser(opt)
    p.parse()

def parse_args():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("--file", required=True,
                        help="bin file which needed to be parsed.")
    arg_parser.add_argument("--keyword", required=True,
                        help="the lines contains the 'keyword' will be chosn to parse.")
    arg_parser.add_argument("--pattern", required=True,
                        help="the parse pattern needed to parse the lines.")

    return arg_parser.parse_args()

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

import argparse
import os
import subprocess

def parse_args():

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("directory",
                             help="specify the directory.")
    arg_parser.add_argument("-b", "--bin", required=True,
                             help="specify the executive file needed to run.")

    return arg_parser.parse_args()

def print_args(args):
    bin_file = os.path.join(os.getcwd(), args.bin)
    dir_name = os.path.join(os.getcwd(), args.directory)
    print bin_file
    print dir_name

def batch_process_ttitrace(dir):
    for f in os.listdir(dir):
        source_file = os.path.join(dir, f)
        target_file = os.path.join(dir, f[:f.find(".")] + ".csv")
        command = "tti_trace_parser_wmp.exe --decode %s --output %s" %(source_file, target_file)

        subprocess.call(command)

def main():
    args = parse_args()
    print_args(args)

    if args.bin == "tti_trace_parser_wmp.exe":
        batch_process_ttitrace(args.directory)
    else:
        pass


if __name__ == "__main__":
    main()

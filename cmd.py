# -*- encoding: utf-8 -*-

import argparse
import sys

def get_argument_parser():
    parser = argparse.ArgumentParser(prog='jeni')
    parser.add_argument('--version', action='version', version=get_version())
    return parser

def get_version():
    return "jeni 0.0.1"

def main():
    parser = get_argument_parser()
    if len(sys.argv) == 1:
        parser.print_help()
    parser.parse_args()

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)

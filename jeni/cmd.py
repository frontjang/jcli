# Copyright 2016 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import sys

import core
import parse


def main():
    """Main program"""
    manager = core.Manager()
    parser = parse.get_argument_parser()

    # Print help if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
    # Parse arguments
    args = parser.parse_args(sys.argv[1:])
    action = args.action
    # Run actio
    manager.run_action(action)


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)

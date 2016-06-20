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

import argparse
import config
from executor.job import Job
import getpass
import sys


def get_version():
    """Returns jeni version."""
    return "Jeni 0.0.1"


def create_parser():
    """Returns argument parser"""

    # Jeni top level arguments
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--user', '-u', default=getpass.getuser(),
                               help='username')
    parent_parser.add_argument('--config', '-c', dest="config",
                               help='jeni configuration file')
    parent_parser.add_argument('--debug', required=False, action='store_true',
                               dest="debug", help='debug flag')

    main_parser = argparse.ArgumentParser()
    jeni_subparsers = main_parser.add_subparsers(title="jeni",
                                                 dest="main_command")

    # Job parser
    job_parser = jeni_subparsers.add_parser("job", parents=[parent_parser])
    job_action_subparser = job_parser.add_subparsers(title="action",
                                                     dest="job_command")

    # Job sub commands (count, list, delete)
    job_action_subparser.add_parser(
        "count", help="Number of jobs", parents=[parent_parser])
    job_list_parser = job_action_subparser.add_parser(
        "list", help="list job(s)", parents=[parent_parser])
    job_list_parser.add_argument('name', help='part of the job name',
                                 nargs='?')
    job_delete_parser = job_action_subparser.add_parser(
        "delete", help="delete job", parents=[parent_parser])
    job_delete_parser.add_argument('name',
                                   help='the name of the job to delete')

    return main_parser


def main():
    """Jeni Main Entry."""

    # Parse arguments provided by the user
    parser = create_parser()
    args = parser.parse_args()

    # Set config object that will hold information on the Jenkins server
    run_config = config.read(args.config)

    # Get url, user and password to be able setup connection to the server
    url = config.get_value(run_config, 'jenkins', 'url')
    user = config.get_value(run_config, 'jenkins', 'user')
    password = config.get_value(run_config, 'jenkins', 'password')

    if args.main_command == 'job':
        job_executor = Job(args.job_command, url, user, password, args.name)
        job_executor.run()

if __name__ == '__main__':
    sys.exit(main())

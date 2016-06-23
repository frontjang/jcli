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
from executor.node import Node
from executor.view import View
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

    # Job sub-commands (count, list, delete)
    job_action_subparser.add_parser(
        "count", help="print number of jobs", parents=[parent_parser])
    job_list_parser = job_action_subparser.add_parser(
        "list", help="list job(s)", parents=[parent_parser])
    job_list_parser.add_argument('name', help='job name or part of it',
                                 nargs='?')
    job_delete_parser = job_action_subparser.add_parser(
        "delete", help="delete job", parents=[parent_parser])
    job_delete_parser.add_argument('name',
                                   help='the name of the job to delete')
    job_build_parser = job_action_subparser.add_parser(
        "build", help="build job", parents=[parent_parser])
    job_build_parser.add_argument(
        'name', help='the name of the job to build')
    job_build_parser.add_argument(
        '-p', '--parameters', type=str, help='params for parameterized job')

    # View parser
    view_parser = jeni_subparsers.add_parser("view", parents=[parent_parser])
    view_action_subparser = view_parser.add_subparsers(title="action",
                                                       dest="view_command")

    # View sub-commands
    view_list_parser = view_action_subparser.add_parser(
        "list", help="list view(s)", parents=[parent_parser])
    view_list_parser.add_argument('name', help='view name or part of it',
                                  nargs='?')
    view_delete_parser = view_action_subparser.add_parser(
        "delete", help="delete view", parents=[parent_parser])
    view_delete_parser.add_argument('name',
                                    help='the name of the view to delete')

    # Node parser
    node_parser = jeni_subparsers.add_parser("node", parents=[parent_parser])
    node_action_subparser = node_parser.add_subparsers(title="action",
                                                       dest="node_command")

    # Node sub-commands
    node_list_parser = node_action_subparser.add_parser(
        "list", help="list node(s)", parents=[parent_parser])
    node_list_parser.add_argument('name', help='node name or part of it',
                                  nargs='?')
    node_delete_parser = node_action_subparser.add_parser(
        "delete", help="delete node", parents=[parent_parser])
    node_delete_parser.add_argument('name',
                                    help='the name of the node to delete')

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

    # 'job' command
    if args.main_command == 'job':
        job_executor = Job(args.job_command, url, user, password, args)
        job_executor.run()

    # 'view' command
    if args.main_command == 'view':
        view_executor = View(args.view_command, url, user, password, args)
        view_executor.run()

    # 'node' command
    if args.main_command == 'node':
        node_executor = Node(args.node_command, url, user, password, args)
        node_executor.run()

if __name__ == '__main__':
    sys.exit(main())

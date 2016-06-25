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
import getpass


def create_job_parser(client_subparsers, parent_parser):
    """Creates job parser"""

    job_parser = client_subparsers.add_parser("job", parents=[parent_parser])
    job_action_subparser = job_parser.add_subparsers(title="action",
                                                     dest="job_command")
    # Job sub-commands
    # Count
    job_action_subparser.add_parser(
        "count", help="print number of jobs", parents=[parent_parser])
    # List
    job_list_parser = job_action_subparser.add_parser(
        "list", help="list job(s)", parents=[parent_parser])
    job_list_parser.add_argument('name', help='job name or part of it',
                                 nargs='?')
    # Delete
    job_delete_parser = job_action_subparser.add_parser(
        "delete", help="delete job", parents=[parent_parser])
    job_delete_parser.add_argument('name',
                                   help='the name of the job to delete')
    # Build job
    job_build_parser = job_action_subparser.add_parser(
        "build", help="build job", parents=[parent_parser])
    job_build_parser.add_argument(
        'name', help='the name of the job to build')
    job_build_parser.add_argument(
        '-p', '--parameters', type=str, help='params for parameterized job')
    # Copy job
    job_copy_parser = job_action_subparser.add_parser(
        "copy", help="copy job", parents=[parent_parser])
    job_copy_parser.add_argument(
        'source_job_name', help='the name of the job to copy')
    job_copy_parser.add_argument(
        'dest_job_name', help='the name of the new job')
    # Disable job
    job_disable_parser = job_action_subparser.add_parser(
        "disable", help="disable job", parents=[parent_parser])
    job_disable_parser.add_argument(
        'name', help='the name of the job to disable')
    # Enable job
    job_enable_parser = job_action_subparser.add_parser(
        "enable", help="enables job", parents=[parent_parser])
    job_enable_parser.add_argument('name',
                                   help='the name of the job to enable')
    # Print information on last build
    job_last_build_parser = job_action_subparser.add_parser(
        "last_build", help="Print information on last build",
        parents=[parent_parser])
    job_last_build_parser.add_argument(
        'name', help='the name of the job')


def create_view_parser(client_subparsers, parent_parser):
    """Creates view parser"""

    view_parser = client_subparsers.add_parser("view", parents=[parent_parser])
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
    view_jobs_parser = view_action_subparser.add_parser(
        "jobs",
        help="List all the jobs under specific view", parents=[parent_parser])
    view_jobs_parser.add_argument(
        'name', help='the name of the view')
    view_create_parser = view_action_subparser.add_parser(
        "create", help="create view", parents=[parent_parser])
    view_create_parser.add_argument(
        'name', help='name of the view', nargs='?')


def create_node_parser(client_subparsers, parent_parser):
    """Creates node parser"""

    # Node parser
    node_parser = client_subparsers.add_parser("node", parents=[parent_parser])
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


def create_parser():
    """Returns argument parser"""

    # Jcli top level parser
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--user', '-u', default=getpass.getuser(),
                               help='username')
    parent_parser.add_argument('--config', '-c', dest="config",
                               help='client configuration file')
    parent_parser.add_argument('--debug', required=False, action='store_true',
                               dest="debug", help='debug flag')

    main_parser = argparse.ArgumentParser()
    client_subparsers = main_parser.add_subparsers(
        title="client", dest="main_command")

    create_job_parser(client_subparsers, parent_parser)
    create_view_parser(client_subparsers, parent_parser)
    create_node_parser(client_subparsers, parent_parser)

    return main_parser

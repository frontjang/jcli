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

import config
from executor.job import Job
from executor.node import Node
from executor.plugin import Plugin
from executor.view import View
import parse


def main():
    """Jcli Main Entry."""

    # Parse arguments provided by the user
    parser = parse.create_parser()
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

    # 'plugin' command
    if args.main_command == 'plugin':
        plugin_executor = Plugin(args.plugin_command, url, user, password, args)
        plugin_executor.run()

if __name__ == '__main__':
    sys.exit(main())

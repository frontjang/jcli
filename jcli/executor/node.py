#!/usr/bin/env python
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

import logging

from jcli import errors
from server import Server

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()


class Node(Server):
    """Manages node command execution"""

    def __init__(self, action, url, user, password, node_args):
        super(Node, self).__init__(url, user, password)
        self.action = action
        self.node_args = node_args

    def get_nodes_names(self):
        """Returns list of all nodes name"""

        nodes_names = []

        nodes = self.server.get_nodes()
        if self.node_args.name:
            for node_object in nodes:
                if self.node_args.name in node_object['name']:
                    nodes_names.append(node_object['name'])
        else:
            for node_object in nodes:
                nodes_names.append(node_object['name'])

        return nodes_names

    def delete_node(self):
        """Removes node from the server"""

        if self.name:
            try:
                self.server.delete_node(self.node_args.name)
            except Exception:
                raise errors.JcliException(
                    "No such node: {}".format(self.node_args.name))
            logger.info("Removed node: {}".format(self.node_args.name))
        else:
            logger.info("No name provided. Exiting...")

    def run(self):
        """Executes chosen action."""

        if self.action == 'list':
            for node in self.get_nodes_names():
                logger.info(node)

        if self.action == 'delete':
            self.delete_node()

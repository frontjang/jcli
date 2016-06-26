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

import jenkins
import logging

from jcli import errors
from server import Server

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()


class Plugin(Server):
    """Manages plugin command execution"""

    def __init__(self, action, url, user, password, plugin_args):
        super(Plugin, self).__init__(url, user, password)
        self.action = action
        self.plugin_args = plugin_args

    def list_plugins(self):
        """Print list of plugins"""

        try:
            plugins = self.server.get_plugins()

            if self.plugin_args.name:
                for name, info in plugins.items():
                    if self.plugin_args.name in name[0]:
                        logger.info("Name: {}".format(info['longName']))
                        logger.info("Enabled?: {}".format(info['enabled']))
                        logger.info("Has update?: {}".format(info['hasUpdate']))
                        logger.info("URL: {}".format(info['url']))
                        logger.info("Version: {}\n".format(info['version']))
            else:
                for name,info in plugins.items():
                    logger.info(name[0])

        except Exception as e:
            raise errors.JcliException(e)

    def run(self):
        """Executes chosen action."""

        if self.action == 'list':
            self.list_plugins()

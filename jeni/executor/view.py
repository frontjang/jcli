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

import jeni.errors as errors
import logging
from server import Server

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()


class View(Server):
    """Manages view command execution"""

    def __init__(self, action, url, user, password, name=None):
        super(View, self).__init__(url, user, password)
        self.action = action
        self.name = name

    def get_views_names(self):
        """Returns list of all views name"""

        views_names = []

        views = self.server.get_views()
        if self.name:
            for view_object in views:
                if self.name in view_object['name']:
                    views_names.append(view_object['name'])
        else:
            for view_object in views:
                views_names.append(view_object['name'])

        return views_names

    def delete_view(self):
        """Removes view from the server"""

        if self.name:
            try:
                self.server.delete_view(self.name)
            except Exception:
                raise errors.JeniException(
                    "No such view: {}".format(self.name))
            logger.info("Removed view: {}".format(self.name))
        else:
            logger.info("No name provided. Exiting...")

    def run(self):
        """Executes chosen action."""

        if self.action == 'list':
            for view in self.get_views_names():
                logger.info(view)

        if self.action == 'delete':
            self.delete_view()
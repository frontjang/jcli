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
from server import Server

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()


class Job(Server):
    """Manages job command execution"""

    def __init__(self, action, url, user, password, name=None):
        super(Job, self).__init__(url, user, password)
        self.action = action
        self.name = name

    def get_jobs_names(self):
        """Returns list of all jobs name"""

        jobs_names = []

        jobs = self.server.get_jobs()
        if self.name:
            for job_object in jobs:
                if self.name in job_object['name']:
                    jobs_names.append(job_object['name'])
        else:
            for job_object in jobs:
                jobs_names.append(job_object['name'])

        return jobs_names

    def run(self):
        """Executes chosen action."""

        for job in self.get_jobs_names():
            logger.info(job)

        if self.action == 'count':
            logger.info("Number of jobs: {}".format(self.server.jobs_count()))

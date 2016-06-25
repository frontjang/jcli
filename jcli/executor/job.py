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

import json
import logging

from jcli import errors
from server import Server

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()


class Job(Server):
    """Manages job command execution"""

    def __init__(self, action, url, user, password, job_args):
        super(Job, self).__init__(url, user, password)
        self.action = action
        self.job_args = job_args

    def get_jobs_names(self):
        """Returns list of all jobs name"""

        jobs_names = []

        jobs = self.server.get_jobs()
        if self.job_args.name:
            for job_object in jobs:
                if self.job_args.name in job_object['name']:
                    jobs_names.append(job_object['name'])
        else:
            for job_object in jobs:
                jobs_names.append(job_object['name'])

        return jobs_names

    def delete_job(self):
        """Removes job from the server"""

        if self.job_args.name:
            try:
                self.server.delete_job(self.job_args.name)
            except Exception:
                raise errors.JcliException(
                    "No such job: {}".format(self.job_args.name))
            logger.info("Removed job: {}".format(self.job_args.name))
        else:
            logger.info("No name provided. Exiting...")

    def disable_job(self):
        """Disables job"""

        try:
            self.server.disable_job(self.job_args.name)

        except Exception:
            raise errors.JcliException(
                "No such job: {}".format(self.job_args.name))

        logger.info("Disabled job: {}".format(self.job_args.name))

    def enable_job(self):
        """Enables job"""

        try:
            self.server.enable_job(self.job_args.name)

        except Exception:
            raise errors.JcliException(
                "No such job: {}".format(self.job_args.name))

        logger.info("Enabled job: {}".format(self.job_args.name))

    def build_job(self):
        """Starts job build"""

        try:
            if self.job_args.parameters:
                self.server.build_job(self.job_args.name,
                                      json.loads(self.job_args.parameters))
                logger.info("Starting job build with parameters: {}".format(
                    self.job_args.name))
            else:
                self.server.build_job(self.job_args.name)
                logger.info("Starting job build without params: {}".format(
                    self.job_args.name))
        except Exception as e:
            raise errors.JcliException(e)

    def copy_job(self):
        """Copies job"""

        try:
            self.server.copy_job(self.job_args.source_job_name,
                                 self.job_args.dest_job_name)
            logger.info("Done copying: {}. The new job is called: {}".format(
                self.job_args.source_job_name, self.job_args.dest_job_name))
        except Exception as e:
            raise errors.JcliException(e)

    def last_build(self):
        """Output information on last build"""

        try:
            last_build_number = self.server.get_job_info(
                self.job_args.name)['lastCompletedBuild']['number']
            build_info = self.server.get_job_info(
                self.job_args.name, last_build_number)
            logger.info(
                "=================== Last build summary ===================\n")
            logger.info("Build Number: {}".format(last_build_number))

            # Log SCMs
            logger.info("\nSCMs:\n")
            for scm in build_info['scm']['configuredSCMs']:
                for info in scm['userRemoteConfigs']:
                    logger.info("  Url: {}".format(info['url']))
                    logger.info(
                        "  Refspec: {}\n  -----".format(info['refspec']))

            # Log Parameters
            logger.info("\n\nParameters:\n")
            for param in build_info['property'][6]['parameterDefinitions']:
                logger.info("  Parameter: {}\n  Value: {}\n  -----".format(
                    param['defaultParameterValue']['name'],
                    param['defaultParameterValue']['value']))

            # Log general build info
            logger.info("\n\nBuild Duration: {}".format(
                build_info['lastBuild']['duration']))
            logger.info("Built on slave: {}".format(
                build_info['lastBuild']['builtOn']))
            logger.info("URL: {}".format(build_info['lastBuild']['url']))
            logger.info(
                "\nResult: {}".format(build_info['lastBuild']['result']))

        except Exception as e:
            raise errors.JcliException(e)

    def run(self):
        """Executes chosen action."""

        if self.action == 'list':
            for job in self.get_jobs_names():
                logger.info(job)

        if self.action == 'count':
            logger.info("Number of jobs: {}".format(self.server.jobs_count()))

        if self.action == 'delete':
            self.delete_job()

        if self.action == 'build':
            self.build_job()

        if self.action == 'copy':
            self.copy_job()

        if self.action == 'disable':
            self.disable_job()

        if self.action == 'enable':
            self.enable_job()

        if self.action == 'last_build':
            self.last_build()

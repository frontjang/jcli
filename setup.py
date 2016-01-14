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

from jeni import __version__
import re
import setuptools


def requires():
    try:
        reqs = map(str.strip, open('requirements.txt').readlines())
        reqs = filter(lambda s: re.match('\w', s), reqs)
        return reqs
    except Exception:
        pass
    return []

setuptools.setup(
    name='jeni',
    version=__version__,
    description='Jenkins swiss knife',
    author='Arie Bregman',
    author_email='abregman@redhat.com',
    url='https://github.com/abregman/jeni',
    packages=['jeni'],
    install_requires=requires(),
    entry_points={
        "console_scripts": ["jeni = jeni.cmd:main"]
    }
)

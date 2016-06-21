Jeni
====

Jenkins Swiss Knife

Install
-------

To install Jeni on your system, run the following command:

    sudo pip install .

Setup config
------------

Jeni is using configuartion file to connect the server.

It can be setup in one of the following paths:

    /etc/jenkins/jeni.conf
    `pwd`/jeni.conf

or it can passed as an argument.

Minimal configuartion is:

    [jenkins]
    user=<jenkins_user>
    password=<api_token>
    url=<jenkins_url>

Examples
--------

### Job examples

Print list of all the jobs:

    python jeni/cmd.py job list

Print jobs which contain the string 'coreci' in their names:

    python jeni/cmd.py job list coreci

Print the number of jobs on Jenkins server:

    python jeni/cmd.py job count

Delete job:
   
    python jeni/cmd.py job delete <job_name>

### View examples

List all views:

    python jeni/cmd.py view list

List views that contain the string 'hello':

    python jeni/cmd.py view list hello

Delete view:

    python jeni/cmd.py view delete <view_name>

License
-------

Apache

Author Information
------------------

Arie Bregman - abregman@redhat.com

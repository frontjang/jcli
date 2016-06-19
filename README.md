Jeni
====

Jenkins Swiss Knife

Requirements
------------

Install requirements with:

    pip install -r requirements.txt

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

Print the number of jobs on Jenkins server:

    python jeni/cmd.py job count

License
-------

Apache

Author Information
------------------

Arie Bregman - abregman@redhat.com

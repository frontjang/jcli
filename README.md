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

    jeni job list

Print jobs which contain the string 'coreci' in their names:

    jeni job list coreci

Print the number of jobs on Jenkins server:

    jeni job count

Delete job:
   
    jeni job delete <job_name>

Build parameterized job:
    jeni job build <job_name> -p '{"GERRIT_REFSPEC": "my_refspec", "GERRIT_BRANCH": "my_branch", "Cleanup_provisioned_resources":"true"}'

### View examples

List all views:

    jeni view list

List views that contain the string 'hello':

    jeni view list hello

Delete view:

    jeni view delete <view_name>

### Node examples

List all nodes:

    jeni node list

Delete node:

    jeni node delete <node_name>

License
-------

Apache

Author Information
------------------

Arie Bregman - abregman@redhat.com

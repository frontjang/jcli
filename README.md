Jcli - Jenkins Command-line Interface
=====================================

The ultimate Jenkins ClI ;)

Install
-------

To install jcli on your system, run the following command:

    sudo pip install .

Setup config
------------

jcli is using configuartion file to connect the server.

It can be setup in one of the following paths:

    /etc/jcli/config.ini
    `pwd`/config.ini

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

    jcli job list

Print jobs which contain the string 'coreci' in their names:

    jcli job list coreci

Print the number of jobs on Jenkins server:

    jcli job count

Delete job:
   
    jcli job delete <job_name>

Build parameterized job:

    jcli job build <job_name> -p '{"GERRIT_REFSPEC": "my_refspec", "GERRIT_BRANCH": "my_branch", "Cleanup_provisioned_resources":"true"}'

Copy job:

    jcli job copy my_current_job my_new_awesome_job

Disable job:

    jcli job disable my_job

Enable job:

    jcli job enable his_job

Print information on last build of specific job:

    jcli job last_build super-mario-job

### View examples

List all views:

    jcli view list

List views that contain the string 'hello':

    jcli view list hello

Delete view:

    jcli view delete view90 

List all the jobs under specific view:

    jcli view jobs view1

Create new view:

    jcli view create new_view

### Node examples

List all nodes:

    jcli node list

Delete node:

    jcli node delete <node_name>

License
-------

Apache

Author Information
------------------

Arie Bregman - abregman@redhat.com

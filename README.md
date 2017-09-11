[![CircleCI](https://circleci.com/gh/cloudify-examples/mariadb-blueprint.svg?style=svg)](https://circleci.com/gh/cloudify-examples/mariadb)

# MariaDB Blueprint

This blueprint deploys a MariaDB Database using Cloudify.

## prerequisites

You will need a *Cloudify Manager* running in either AWS, Azure, Openstack, or GCP.

If you have not already, set up the [example Cloudify environment](https://github.com/cloudify-examples/cloudify-environment-setup). Installing that blueprint and following all of the configuration instructions will ensure you have all of the prerequisites, including keys, plugins, and secrets.

### Step 1: Install the MariaDB Database

In this step, you will run a *Cloudify CLI* command, which uploads the mariadb blueprint to the manager, creates a deployment, and starts an install workflow.

When it is finished, you will be able to play with the wine store application.

#### For AWS run:

```shell
$ cfy install \
    https://github.com/cloudify-examples/mariadb-blueprint/archive/4.1.1.zip \
    -b mariadb \
    -n aws-blueprint.yaml
```


#### For Azure run:

```shell
$ cfy install \
    https://github.com/cloudify-examples/mariadb-blueprint/archive/4.1.1.zip \
    -b mariadb \
    -n azure-blueprint.yaml
```


#### For Openstack run:

```shell
$ cfy install \
    https://github.com/cloudify-examples/mariadb-blueprint/archive/4.1.1.zip \
    -b mariadb \
    -n openstack-blueprint.yaml
```


You should see something like this when you execute the command:

```shell
$ cfy install \
>     https://github.com/cloudify-examples/mariadb-blueprint/archive/4.1.1.zip \
>     -b mariadb \
>     -n aws-blueprint.yaml
Downloading https://github.com/cloudify-examples/mariadb-blueprint/archive/4.1.1.zip to ...
Uploading blueprint /.../mariadb-4.1.1/aws-blueprint.yaml...
 aws-blueprint.yaml |##################################################| 100.0%
Blueprint uploaded. The blueprint's id is mariadb
Creating new deployment from blueprint demo...
Deployment created. The deployment's id is mariadb
Executing workflow install on deployment mariadb [timeout=900 seconds]
Deployment environment creation is in progress...
2017-05-01 00:00:00.000  CFY <mariadb> Starting 'install' workflow execution
...
...
...
2017-05-01 00:05:00.000  CFY <mariadb> 'install' workflow execution succeeded
```


### Step 2: Verify the demo installed and started.

Once the workflow execution is complete, we can view the application endpoint by running: <br>

```shell
$ cfy deployments outputs mariadb
```

You should see an output like this:

```shell
Retrieving outputs for deployment demo...
 - "ip":
     Description: Public IP Address
     Value: 10.239.0.18
```

You can now connect to the MariaDB on that IP.

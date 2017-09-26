[![CircleCI](https://circleci.com/gh/cloudify-examples/mariadb-blueprint.svg?style=svg)](https://circleci.com/gh/cloudify-examples/mariadb)

# MariaDB Blueprint

This blueprint deploys a [MariaDB database cluster with Galera](https://mariadb.com/kb/en/library/what-is-mariadb-galera-cluster/) using Cloudify.


## prerequisites

You will need a *Cloudify Manager* running in either AWS, Azure, Openstack, or GCP.

If you have not already, set up the [example Cloudify environment](https://github.com/cloudify-examples/cloudify-environment-setup). Installing that blueprint and following all of the configuration instructions will ensure you have all of the prerequisites, including keys, plugins, and secrets.


### Step 1: Install the MariaDB database cluster with Galera

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

#### For GCP run:

```shell
$ cfy install \
    https://github.com/cloudify-examples/mariadb-blueprint/archive/4.1.1.zip \
    -b mariadb \
    -n gcp-blueprint.yaml
```


You should see something like this when you execute the command:


```shell
  ::  cfy install mariadb-blueprint/openstack-blueprint.yaml -b mariadb
Uploading blueprint mariadb-blueprint/openstack-blueprint.yaml...
 openstack-bluepri... |################################################| 100.0%
Blueprint uploaded. The blueprint's id is mariadb
Creating new deployment from blueprint mariadb...
Deployment created. The deployment's id is mariadb
Executing workflow install on deployment mariadb [timeout=900 seconds]
```


### Step 2: Verify the demo installed and started.

Once the workflow execution is complete, we can view the application endpoint by running: <br>

```shell
cfy deployments outputs mariadb
Retrieving outputs for deployment mariadb...
 - "cluster_addresses":
     Description: Cluster Addresses
     Value: [u'192.168.121.11']
 - "master":
     Description: master node ip
     Value: 192.168.121.11
```


### Step 3: Verify the cluster has started:

SSH into the VM and execute `mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"`:

```
[centos@cloudify ~]$ ssh -i ~/.ssh/agent.key centos@192.168.121.11
The authenticity of host '192.168.121.11 (192.168.121.11)' can't be established.
ECDSA key fingerprint is f1:35:95:b9:57:51:5a:b8:ac:13:79:6e:1a:80:c2:ed.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.121.11' (ECDSA) to the list of known hosts.
Last login: Tue Sep 26 10:14:39 2017
[centos@server-galera-host-7ituuu ~]$ mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
Enter password:
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 1     |
+--------------------+-------+
```

__The default password is `new_password`.__

__Hint: Modify the MySQL command to see more info about the cluster, example: `SHOW STATUS LIKE 'wsrep%'`.__


### Step 4: Scale the cluster:

```
cfy executions start scale -d mariadb -p scalable_entity_name=app_group
```

When the scale workflow has succeeded, you can follow Step 3 again to see the cluster size has increased.

```
[centos@cloudify ~]$ ssh -i ~/.ssh/agent.key centos@192.168.121.11
Last login: Tue Sep 26 10:24:02 2017 from 192.168.120.5
[centos@server-galera-host-7ituuu ~]$ mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
Enter password:
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 2     |
+--------------------+-------+
```

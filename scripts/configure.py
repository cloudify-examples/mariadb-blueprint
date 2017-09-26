#!/usr/bin/env python

import os
from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

try:
    import mysql.connector as mariadb
except ImportError:
    import pip
    pip.main(['install', 'mysql-connector-python-rf'])
    import mysql.connector as mariadb


if __name__ == '__main__':

    old_password = inputs.get('old_password', str())
    new_password = inputs.get('new_password', old_password)
    users = inputs.get('new_users', {})

    db = mariadb.connect(user='root', passwd=old_password, db='mysql')
    cur = db.cursor()

    cur.execute("UPDATE mysql.user SET Password = PASSWORD('{0}') WHERE User = 'root'".format(new_password))
    cur.execute("DROP USER ''@'localhost'")
    cur.execute("DROP USER ''@'{0}'".format(os.uname()[1]))
    cur.execute("DROP DATABASE test")

    for username, userdescription in users.items():

        create_user = "CREATE USER '{0}'@'{1}' IDENTIFIED BY '{2}';".format(
            username,
            userdescription.get('host', '%'),
            userdescription.get('password', new_password))

        create_user_grant = "GRANT {0} ON {1} TO '{2}'@'{3}' WITH GRANT OPTION;".format(
            'ALL PRIVILEGES' if userdescription.get('privileges')[0] == 'ALL PRIVILEGES' else ', '.join(userdescription.get('privileges')),
            userdescription.get('database', '*.*'),
            username,
            userdescription.get('host', '%'))

        ctx.logger.debug(create_user)
        ctx.logger.debug(create_user_grant)

        cur.execute(create_user)
        cur.execute(create_user_grant)

    cur.execute("FLUSH PRIVILEGES")
    db.close()

#!/usr/bin/env python

import os
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

    db = mariadb.connect(user='root', passwd=old_password, db='mysql')
    cur = db.cursor()
    cur.execute("UPDATE mysql.user SET Password = PASSWORD('{0}') WHERE User = 'root'".format(new_password))
    cur.execute("DROP USER ''@'localhost'")
    cur.execute("DROP USER ''@'{0}'".format(os.uname()[1]))
    cur.execute("DROP DATABASE test")
    cur.execute("FLUSH PRIVILEGES")
    db.close()

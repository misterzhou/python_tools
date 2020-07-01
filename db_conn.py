#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: mason
# Date: 2014-10-29
# Filename: db_conn.py
# Purpose: 数据库连接

'''
DB Connection Mysql数据库链接
注：需安装Mysql驱动: mysql-connector-python'
'''

__author__ = 'mason'

import mysql.connector

class DBConn(object):

    conn = None
    cur = None

    def __init__(self, user, password, database, host):
        '''Init parameters'''
        self.user = user
        self.password = password
        self.database = database
        self.host = host

    def query(self, sql, tuple_args):
        '''select resultset from database'''
        try:
            conn = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
            cur = conn.cursor()
            cur.execute(sql, tuple_args)
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except Exception, e:
            print e
            return
    def query_without_args(self, sql):
        return self.query(sql, None)



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: guojing
# Date: 2014-10-29
# Filename: db_conn.py
# Purpose: 数据库连接

'''
DB Connection Mysql数据库链接
注：需安装Mysql驱动: mysql-connector-python'
'''

__author__ = 'guojing'

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

	def query(self, sql, param):
		'''select resultset from database'''
		try:
			conn = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
			cur = conn.cursor()
			cur.execute(sql, (param,))
			datas = cur.fetchall()
			cur.close()
			conn.close()
			return datas
		except Exception, e:
			print e
			return 


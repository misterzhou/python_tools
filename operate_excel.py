#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: guojing
# Date: 2014-10-29
# Filename: operate_excel.py

'''
python读写Excel
Require: 需要先安装Python模块: xlrd xlwt xlutils
'''

__author__ = 'guojing'

from xlrd import open_workbook
from xlwt import easyxf
from xlutils.copy import copy

class Excel(object):

	#def __init__(self):


	def write(self, datas, tpl_filename, save_path):
		'''
		Args:
		  datas: 从数据库获取的结果集(list)
		  save_path: 生成的excel文件名
		  tpl_filename: excel模板
		'''
		tpl = open_workbook(tpl_filename, formatting_info=True)
		tpl_sheet = tpl.sheet_by_index(0) #read only
		nrows = tpl_sheet.nrows
		ncols = tpl_sheet.ncols
		target = copy(tpl)
		sheet = target.get_sheet(0) # a writable copy
		size = len(datas)
		for row in xrange(0,size - 1):
			for col in xrange(0, ncols):
				sheet.write(row + 1, col, datas[row][col])
		target.save(save_path)

		
	
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
import xlwt
#from xlwt import easyxf
from xlutils.copy import copy

class Excel(object):

    #def __init__(self):

    def write(self, tpl, dest_file, *tuple_args):
        # 单元格样式
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = 'SimSun' #设置字体
        style.font = font
        tpl_book = open_workbook(tpl, formatting_info=True)
        target = copy(tpl_book)
        i = 0
        for arg in tuple_args:
            sheet = target.get_sheet(i) # a writable copy
            i += 1
            size = len(arg)
            cols = len(arg[0])
            for row in xrange(0,size):
                for col in xrange(0, cols):
                    sheet.write(row + 1, col, arg[row][col], style)
        target.save(dest_file)

    # def write(self, tpl, dest_file, datas):
    #     '''
    #     Args:
    #       datas: 从数据库获取的结果集(list)
    #       dest_file: 生成的excel文件名
    #       tpl: excel模板
    #     '''
    #     tpl_book = open_workbook(tpl, formatting_info=True)
    #     tpl_sheet = tpl_book.sheet_by_index(0) #read only
    #     nrows = tpl_sheet.nrows
    #     ncols = tpl_sheet.ncols
    #     target = copy(tpl_book)
    #     sheet = target.get_sheet(0) # a writable copy
    #     style = xlwt.XFStyle()
    #     font = xlwt.Font()
    #     font.name = 'SimSun' #设置字体
    #     style.font = font
    #     size = len(datas)
    #     for row in xrange(0,size):
    #         for col in xrange(0, ncols):
    #             sheet.write(row + 1, col, datas[row][col], style)
    #     target.save(dest_file)

        
    

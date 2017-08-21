# _*_coding:utf-8
from database.Database import *  # 导入数据


class Model(object):
    '''模型层'''

    def get_quote(self, index):
        '''根据索引读取数据
        @parameter index 索引值
        '''
        try:
            valve = Arrays[index]
        except IndexError as err:
            valve = '未找到该名人名言'
        return valve
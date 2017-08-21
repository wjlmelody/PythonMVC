# _*_coding:utf-8
from database.database import *  # 导入数据


class Model(object):
    '''模型层'''

    def get_quote(self, index):
        '''根据索引读取数据
        @parameter index 索引值
        '''
        try:
            valve = Arrays[index]
        except IndexError as err:
            valve = 'Not Found!'
        return valve
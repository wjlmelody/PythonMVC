# _*_coding:utf-8

class View(object):
    '''视图层'''

    def show(self, quote):
        '''显示查询结果
        @parameter quote 接收数据'''
        print('您查询到的名人名言是:%s' % (quote))

    def error(self, msg):
        '''打印错误消息
        @msg msg 接收错误消息'''
        print("error: %s" % (msg))

    def select_quote(self):
        '''读取用户的选择'''
        return raw_input("请输入编号进行查询:")
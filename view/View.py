# _*_coding:utf-8

import sys
from view.show import Ui_Show
from view.select import Ui_Select
from PyQt5 import QtWidgets

class View(object):
    '''视图层'''
    def __init__(self):
        pass

    def show(self, quote):
        # '''显示查询结果
        # @parameter quote 接收数据'''
        # print('您查询到的名人名言是:%s' % (quote))
        Str_show = "您查询到的名人名言是:\n"
        Str_show += quote

        app = QtWidgets.QApplication(sys.argv)
        myshow = Window_show()
        myshow.setWindowTitle('名人名言显示')
        myshow.textBrowser.setText(Str_show)
        myshow.pushButton.clicked.connect(app.quit)
        myshow.show()
        sys.exit(app.exec_())

    def error(self, msg):
        '''打印错误消息
        @msg msg 接收错误消息'''
        Str_show = "错误类型为：\n"
        Str_show += msg

        app = QtWidgets.QApplication(sys.argv)
        myshow = Window_show()
        myshow.setWindowTitle('错误提示')
        myshow.textBrowser.setText(Str_show)
        myshow.pushButton.clicked.connect(app.quit)
        myshow.show()
        sys.exit(app.exec_())

    def select_quote(self):
        '''读取用户的选择'''
        # return input("请输入编号进行查询:")

        app = QtWidgets.QApplication(sys.argv)
        myselect = Window_select()
        myselect.setWindowTitle('名人名言查询')
        myselect.show()

        if app.exec_():
            result = myselect.btnClick()
            print(result)
            return result



    # def select_button(self, myselect, app, selectString):
    #     # self.lineEdit.displayText().emit()
    #     selectString.append(myselect.lineEdit.displayText())
    #     print (self.selectString)
    #     app.quit()

class Window_show(QtWidgets.QWidget, Ui_Show):
    def __init__(self):
        super(Window_show, self).__init__()
        self.setupUi(self)

class Window_select(QtWidgets.QWidget, Ui_Select):
    def __init__(self):
        super(Window_select, self).__init__()
        self.setupUi(self)
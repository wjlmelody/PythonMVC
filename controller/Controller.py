# _*_coding:utf-8

import sys
from model.Model import Model
from view.show import Ui_Show
from view.select import Ui_Select
from PyQt5 import QtWidgets, QtGui

class Controller(QtWidgets.QWidget):
    def __init__(self):
        super(Controller, self).__init__()
        self.Ui = Ui_Select()
        self.model = Model()
        self.Ui.setupUi(self)
        self.setWindowTitle('名人名言检索')

        self.select_str = ""
        self.Ui.pushButton.clicked.connect(self.btn_clicked_select)

    def btn_clicked_select(self):
        self.select_str = self.Ui.lineEdit.text()

        try:
            index = int(self.select_str)
            quote = self.model.get_quote(index)
            self.show_quote(quote)
        except ValueError:
            self.error_quote('索引值不合法')

    def show_quote(self, quote):
        self.subwindow = Ui_Show()
        self.dialog = QtWidgets.QDialog(self)
        self.subwindow.setupUi(self.dialog)
        self.dialog.setWindowTitle('名人名言显示')
        self.subwindow.textBrowser.setText(quote)
        self.subwindow.pushButton.clicked.connect(self.btn_clicked_show)
        self.dialog.exec_()

    def error_quote(self, quote):
        self.subwindow = Ui_Show()
        self.dialog = QtWidgets.QDialog(self)
        self.subwindow.setupUi(self.dialog)
        self.dialog.setWindowTitle('错误提示')
        self.subwindow.textBrowser.setText(quote)
        self.subwindow.pushButton.clicked.connect(self.btn_clicked_show)
        self.dialog.exec_()

    def btn_clicked_show(self):
        self.dialog.close()

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     MainApp = View()
#     MainApp.show()
#     sys.exit(app.exec_())

# class Controller(object):
#     '''控制器层'''
#
#     def __init__(self):
#         self.model = Model()
#         self.view = View()
#
#     def run(self):
#         app = QtWidgets.QApplication()
#         MainApp = self.view
#         MainApp.show()
#         sys.exit(app.exec_())


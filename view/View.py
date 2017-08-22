# _*_coding:utf-8

from model.Model import Model
from view.show import Ui_Show
from view.select import Ui_Select
from PyQt5 import QtWidgets

class View(QtWidgets.QWidget):
    '''视图层'''
    def __init__(self):
        super(View, self).__init__()
        self.Ui = Ui_Select()
        self.model = Model()
        self.Ui.setupUi(self)
        self.setWindowTitle('名人名言检索')

    def show_quote(self, quote):
        self.subwindow = Ui_Show()
        self.dialog = QtWidgets.QDialog(self)
        self.subwindow.setupUi(self.dialog)
        self.dialog.setWindowTitle('名人名言显示')
        self.subwindow.textBrowser.setText(quote)
        self.subwindow.pushButton.clicked.connect(self.dialog.close)
        self.dialog.exec_()

    def error_quote(self, quote):
        self.subwindow = Ui_Show()
        self.dialog = QtWidgets.QDialog(self)
        self.subwindow.setupUi(self.dialog)
        self.dialog.setWindowTitle('错误提示')
        self.subwindow.textBrowser.setText(quote)
        self.subwindow.pushButton.clicked.connect(self.dialog.close)
        self.dialog.exec_()

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     MainApp = View()
#     MainApp.show()
#     sys.exit(app.exec_())



# _*_coding:utf-8
'''主程序'''
import sys

from controller.Controller import Controller
from model.Model import Model
from view.View import View
from view.show import Ui_Show
from view.select import Ui_Select
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainApp = Controller()
    MainApp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
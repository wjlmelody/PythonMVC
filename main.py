# _*_coding:utf-8
'''主程序'''
import sys

from controller.Controller import Controller
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.run()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
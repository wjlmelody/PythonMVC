# _*_coding:utf-8
'''主程序'''
from controller.controller import Controller

def mains():
    while True:
        controller = Controller()
        controller.run()

if __name__ == '__main__':
    mains()
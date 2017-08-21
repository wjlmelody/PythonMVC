# _*_coding:utf-8
from model.model import Model
from view import View

class Controller(object):
    '''控制器层'''

    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        n = self.view.select_quote()
        try:
            index = int(n)
            quote = self.model.get_quote(index)
            self.view.show(quote)
        except ValueError as err:
            self.view.error('不合法的索引值')
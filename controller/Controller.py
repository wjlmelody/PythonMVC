# _*_coding:utf-8

from model.Model import Model
from view.View import View

class Controller(object):
    '''控制器层'''

    def __init__(self):
        self.model = Model()
        self.view = View()
        self.select_str = ""

    def run(self):
        self.view.show()
        self.view.Ui.pushButton.clicked.connect(self.btn_clicked_select)

    def btn_clicked_select(self):
        self.select_str = self.view.Ui.lineEdit.text()

        try:
            index = int(self.select_str)
            quote = self.model.get_quote(index)
            self.view.show_quote(quote)
        except ValueError:
            self.view.error_quote('索引值为空')
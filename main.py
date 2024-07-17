# -*- coding: utf-8 -*-

import os
import re
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config

kivy.require('2.2.0')

# 画面サイズの指定
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '400')

Builder.load_file(os.path.dirname(__file__) + "/interface.kv")


class TextInputTestWidget(Widget):

    def __init__(self, **kwargs):
        super(TextInputTestWidget, self).__init__(**kwargs)


class TextInputTestApp(App):
    def __init__(self, **kwargs):
        super(TextInputTestApp, self).__init__(**kwargs)
        self.title = 'TextInput Test'

    def build(self):
        return TextInputTestWidget()


if __name__ == '__main__':
    app = TextInputTestApp()
    app.run()

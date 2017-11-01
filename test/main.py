# %load ../0_Hello/main.py
from kivy.app import App
from kivy.core.text import LabelBase

LabelBase.register(name='Roboto',
    fn_regular='Roboto-Thin.ttf',
    fn_bold='Roboto-Medium.ttf')

class ClockApp(App):
    pass

if __name__ == '__main__':
    ClockApp().run()
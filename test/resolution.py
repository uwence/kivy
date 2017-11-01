from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import os
os.environ['KIVY_METRICS_DENSITY'] = '1'
os.environ['KIVY_DPI'] = '96'

class Container(Widget):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.size = '800dp','600dp'
        label = Label(text="Am i A Label ?")
        label.size = '100dp','100dp'
        label.pos = '700dp','10dp'
        self.add_widget(label)

class MyJB(App):
    def build(self):

        parent = Container()
        return parent

if __name__ == '__main__':
    MyJB().run()
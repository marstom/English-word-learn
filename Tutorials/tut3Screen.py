'''
Created on 05.03.2017

@author: Tomek
'''
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder

Builder.load_file('./tut3screen.kv')

class Scr1(Screen):
    pass

class Scr2(Screen):
    pass

class Scr3(Screen):
    pass

class ScreenMng(ScreenManager):
    def add(self):
        self.add_widget(Scr1(name='scr1'))
        self.add_widget(Scr2(name='scr2'))
        self.add_widget(Scr3(name='scr3'))
        self.current = 'scr1'
'''
sm = ScreenManager()
sm.add_widget(Scr1(name='scr1'))
sm.add_widget(Scr2(name='scr2'))
sm.current = 'scr2'
'''
class Tut3Screen(App):
    def build(self):
        sm = ScreenMng(transition=FadeTransition())
        sm.add()
        # in kv: app.root.current = 'scr1' to transition
        return sm
    
    
if __name__ == '__main__':
    Tut3Screen().run()
'''
Created on 19.03.2017

@author: Tomek
Tutoial 
-show how to pass argument to button
-show clock usage
-show Animation usage
'''

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.animation import Animation

class Ekran(Widget):
    def __init__(self):
        Widget.__init__(self)
        
    
    def on_button1(self,arg):
        print('b1 {}'.format(arg.text))
        arg.text = 'Zamiana'
        
    def on_button2(self,arg):
        print('guzik2 ')
        #arg.color=[1,1,0,1]
        Animation(color=[1,1,0,1], duration=0.333).start(arg)
        Clock.schedule_once(lambda dt: self.back_to_old(arg),3)
        
    def back_to_old(self,arg):
        arg.color=[1,1,1,1]
        print('change')
        ani=Animation(color=[1,0,1,0], duration=1.)
        ani.start(arg)
        
        
    
class TimerEvent(App):
    def build(self):
        return Ekran()
    
if __name__ == '__main__':
    TimerEvent().run()
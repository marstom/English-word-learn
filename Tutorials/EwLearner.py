from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

class Singularity(Widget):
    napis = StringProperty()
    value = NumericProperty()
    textIn = ObjectProperty(None)
    
    def funkcja1(self):
        self.napis = "teet to jest tekst po angielsku"
        self.value = 250
        #print(self.textIn.gettext())
        
    def textField(self, value):
        pass

class Marvel(Widget):
    pass

class SingularityApp(App):
    def build(self):
        self.load_kv('./learner.kv')
        sin = Singularity()
        sin.funkcja1()
        return sin
    

if __name__ in ('__main__', '__android__'):
    SingularityApp().run()
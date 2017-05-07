'''
Created on 04.03.2017

@author: Tomasz Marszalek
'''


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from gameLogic import GameLogic, SummaryLogic
from kivy.lang import Builder
#from kivy.uix.textinput import TextInput.hint_text_color
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.lang import Builder

INIT_COUNTER = 10

class MainScreen(Screen):
    points = 0
    value = 0
    gameCounter=INIT_COUNTER
    labelText = "English Phrase"
    answers = ['a', 'b', 'c']
    pass

    def __init__(self, **kwargs):
        super(MainScreen,self).__init__(**kwargs)
        
        self.progressBar = self.ids['progressBar']
        self.lPoints = self.ids['lPoints']
        self.lQNumber = self.ids['lQNumber']
        self.lText = self.ids['label_texts']
        self.tIn = self.ids['textIn']
        self.lHint = self.ids['lHint']
        
        self.lText.text=self.answers[0]
        #main screen logic
        self.logic = GameLogic(self)        
    
    def on_validateText(self,napis):
        print(napis)
        ans = self.logic._check_ans(self.tIn.text)
        self.logic.check_goal()
        self.tIn.text=''
        self.logic.animate_background(ans)

        
    def bNext_click(self,arg):
        print('next {}'.format(arg.text))
        self.logic.eval_points(False, True)
        self.logic.animate_background('rBack')
        
        #arg.text = 'hint here for 5 sec'
       

   
class SummaryScreen(Screen):
    def __init__(self,**kwargs):
        super(SummaryScreen, self).__init__(**kwargs)
        self.lWyniki = self.ids['lWyniki'] #label with score table
        self.smlogic = SummaryLogic(self)
    #resets all to initial state
    def bRestart(self):
        self.manager.current = 'Game'
        self.manager.transition.direction = 'right' 
        main = self.manager.get_screen('Game')       
        main.points = 0
        main.gameCounter = INIT_COUNTER
        main.lPoints.text = '0'
        main.lQNumber.text = 'Game: '+ str(INIT_COUNTER)
        main.progressBar.value = 0
        
    def bQuit(self):
        quit()
        
Builder.load_file('englishlearn.kv')

class AppScreens(ScreenManager):
    def add(self):      
        self.add_widget(MainScreen(name="Game") )
        self.add_widget(SummaryScreen(name="Summary"))

        Builder.load_file('englishlearn.kv')
class EnglishLearnMain(App):
    tomek= 22
    def build(self):
        sm = AppScreens()
        sm.add()
        sm.current = 'Game'
        pass
        return sm
if __name__ == '__main__':
    elearn = EnglishLearnMain()
    elearn.run()
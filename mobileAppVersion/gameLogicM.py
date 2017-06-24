'''
Created on 04.03.2017

@author: Tomek
'''

# -*- coding: utf-8 -*-
#import dictParser
from dictParserM.dictParser import DictParser
from scoreWriterM.scoreWriter import ScoreWriter
from kivy.animation import Animation
from kivy.clock import Clock

class GameLogic:
    '''
    
    '''      
    def __init__(self,menu):
        self.menu = menu
        self.loadDictionary('./dictionariesM/dictionary1.csv')
        self.menu.answers = self.dictParser.selectOneItemWithoutRepetitions()
        self.menu.lText.text= self.menu.answers[0]
    
    def loadDictionary(self,filename):
        self.dictParser = DictParser(filename)
    
    def _check_ans(self,ans):
        #ans = ans.decode('utf-8', 'ignore')
        ans = ans.strip()
        ans = ans.lower()
        ans = str(ans)
        isFound = self._compareAnswerToCorrectAnswer(self.menu.answers, ans)
        
        if isFound:  
            self.menu.progressBar.value =0
            self.menu.answers = self.dictParser.selectOneItemWithoutRepetitions()
            self.menu.lText.text= self.menu.answers[0]
            self.menu.points += 1 #add points to player
            self.menu.gameCounter -=1  #game counter increments whatever good or bad answer
            self.menu.lPoints.text = str(self.menu.points)
            self.menu.lQNumber.text = 'Question: '+str(self.menu.gameCounter)
#             print('Dobra odpowiedz!: {} pts: {} game: {}'.format(ans , self.menu.points, self.menu.gameCounter))
            self.eval_points(True, True)
            return 'gBack'
        else:
            self.menu.progressBar.value +=500
            notEnd = self.menu.progressBar.value < 1001
            self.eval_points(False or notEnd, False)
            print(self.menu.answers)
            self.menu.lPoints.text = str(self.menu.points)
#             print('Zla!! odpowiedz!: {} pts: {} game: {}'.format(ans , self.menu.points, self.menu.gameCounter))
            if notEnd:
                return 'yBack'
            else:
                return 'rBack'
                   
    def _compareAnswerToCorrectAnswer(self,lista,toFind):
        #first element is word to display on label, next are answers
        for el in lista:
            el = el.lower()
            el = el.strip()
            if el == toFind and el != lista[0]:
                return True
        return False
        
    def eval_points(self, ans, isNext):
        if ans==False:
            self.menu.lHint.text = self.getAllAnswers()
            Animation(color=[0,1,0,1], duration=1.0).start(self.menu.lHint)
            Clock.schedule_once(lambda fn:Animation(color=[0,1,1,1], duration=1.0).start(self.menu.lHint),1.)
            Clock.schedule_once(lambda fn:Animation(color=[0,0,1,0], duration=1.0).start(self.menu.lHint),3.)
            self.menu.progressBar.value=1001 #overflow bar
            Clock.schedule_once(lambda fn:self._calculate_points(),4.)
            if isNext:
                self.menu.points+=1 #but no substrac point
        else:
            self._calculate_points()

    def getAllAnswers(self):
        str_=''
        answers = iter(self.menu.answers)
        next(answers) #eliminate first answer
        for an in answers:
            str_ += an+', '
        str_ = str_[:-2]
        return str_
    
    def _calculate_points(self):
        if self.menu.progressBar.value > 1000:
            self.menu.progressBar.value =0
            self.menu.points -= 1
            self.menu.gameCounter -=1 #but player have 4 chances
            self.menu.lQNumber.text = 'Question: '+str(self.menu.gameCounter)
            #next question
            self.menu.answers = self.dictParser.selectOneItemWithoutRepetitions()
            self.menu.lText.text= self.menu.answers[0]          
            self.check_goal()
            self.menu.lPoints.text = str(self.menu.points)

    def check_goal(self):
        if self.menu.gameCounter == 0:
            self._displayEndOfGameScreen()
            
    def _displayEndOfGameScreen(self):
        print('END OF GAME')
        #save stats to file 
        writeScore = ScoreWriter('score.csv')
        writeScore.write(self.menu.points, 10, 'dictionary1')
        #next screeen  
        self.menu.manager.current = 'Summary'
        #get from file and display on the screen
        lista = writeScore.read_10pos()
        str_ = writeScore.format_table(lista)
        # display screen - summary
        summ = self.menu.manager.get_screen('Summary')
        summ.lWyniki.text = str_
               
    #visual effect
    def animate_background(self,ans):
        if ans=='gBack':
            self.menu.tIn.background_color=[0,1,0,1]
        elif ans=='rBack':
            self.menu.tIn.background_color=[1,0,0,1]
        elif ans=='yBack':
            self.menu.tIn.background_color = [1,1,0,1]
        Animation(background_color=[1,1,1,1],duration=1.0).start(self.menu.tIn)
            
class SummaryLogic(object):
    points = 0
    def __init__(self, summary):
        self.summary = summary

        
    
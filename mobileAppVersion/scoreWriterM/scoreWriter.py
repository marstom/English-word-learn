'''
Created on 06.03.2017

@author: Tomasz Marszalek
calc;v    ;v                ;calc
<date-now>;<pts>;<questions_number>;<%degree>
<date>;<pts>;<questions_number>;<%degree>
<date>;<pts>;<questions_number>;<%degree>
<date>;<pts>;<questions_number>;<%degree>

#todo, delete record if more than 10 records in file or not? Display only 10 top records
read() -read all
read_10pos() -read only 10pos
write(pts, questions, dictn) - append score to file
format_table() - format string score table
'''
# -*- coding: utf-8 -*-
import datetime

class ScoreWriter(object):
    count = 0
    def __init__(self, filename):
        print('This is score writer mobiles')
        self.filename = filename

    def write(self, pts, questions, dictn):
        fp = open(self.filename, 'a')
        nowTime = datetime.datetime.today().strftime('%d.%m.%Y %H:%M:%S - ')
        # nowTime = '12.12.12 12:12:22 - '
        writ='{};{};{};{};{}\n'.format(nowTime, pts, questions, self._calc_percent(pts,questions), dictn)
        fp.write(writ)
        fp.close()
    
    def _calc_percent(self, pts, questions):
        if pts < 0:
            pts = 0 #eliminate minus percentage
        percent = float(pts)/float(questions)
        return '{}%'.format(int(percent*100.0))
        
    def read(self):
        lista = []
        fp = open(self.filename, 'r')
        for el in fp:
            el=el.strip()
            lista.append(el.split(';'))
        fp.close()
        lista = list(reversed(lista))
        return lista
    
    def read_10pos(self):
        lista = self.read()
        topTen = []
        for i in range(len(lista)):
            topTen.append(lista[i])
            if i >= 8:
                break
        return topTen
    
    def format_table(self,lista):
        str_ = ''
        for el in lista:
            str_ += '{}{}/{}     {}     {}\n'.format(*el)
            #print(lista)
        return str_
        

if __name__ == '__main__':
    sw = ScoreWriter('score.csv')
    sw.write(10, 10, 'kut01')
    re=sw.read_10pos()
    print(sw.format_table(re))
    
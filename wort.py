# coding=utf-8

import case

ARTIKELS = ['der', 'die', 'das']

class Wort:
    def __init__(self, artikel, wort, spanisch=''):
        self.artikel = artikel
        self.wort = wort
        self.spanisch = spanisch

    def __str__(self):
        return self.artikel + ' ' + self.wort


    def checkArtikelGame(self, input, defined=True, c=case.NOMINATIV):
        if(c == case.NOMINATIV):
            if(input==self.getArtikel(defined=defined)):
                return True
            else:
                return False
        if(c == case.AKKUSATIV):
            if(input==self.getArtikel(case.NOMINATIV,defined=defined)):
                return True
            else:
                return False
        if(c == case.DATIV):
            if(input==self.getArtikel(case.DATIV,defined=defined)):
                return True
            else:
                return False


    # Insert check
    def checkArtikel(self):
        if (self.artikel in ARTIKELS):
            return True
        else:
            return False

    def checkWort(self):
        if(len(self.wort.strip())>1):
            return True
        else:
            return False
    

    # Encapsulation
    def setSpanisch(self, spanisch):
        self.spanisch = spanisch

    def getWort(self):
        return self.wort

    def getArtikel(self, c=case.NOMINATIV, defined=True):
        if(c == case.NOMINATIV):
            if(defined):
                return self.artikel
            else:
                if(self.artikel == 'der'):
                    return 'ein'
                if(self.artikel == 'die'):
                    return 'eine'
                if(self.artikel == 'das'):
                    return 'ein'
        if(c == case.AKKUSATIV):
            if(defined):
                if(self.artikel == 'der'):
                    return 'den'
                else:
                    return self.artikel
            else:
                if(self.artikel == 'der'):
                    return 'einen'
                if(self.artikel == 'die'):
                    return 'eine'
                if(self.artikel == 'das'):
                    return 'ein'
        if(c == case.DATIV):
            if(defined):
                if(self.artikel == 'der'):
                    return 'dem'
                if(self.artikel == 'die'):
                    return 'der'
                if(self.artikel == 'das'):
                    return 'dem'
            else:
                if(self.artikel == 'der'):
                    return 'einem'
                if(self.artikel == 'die'):
                    return 'einer'
                if(self.artikel == 'das'):
                    return 'einem'

    def getSpanisch(self):
        return self.spanisch

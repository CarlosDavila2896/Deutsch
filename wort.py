ARTIKELS = ['der', 'die', 'das']

class Wort:
    def __init__(self, artikel, wort, spanisch=''):
        self.artikel = artikel
        self.wort = wort
        self.spanisch = spanisch

    def __str__(self):
        return self.artikel + ' ' + self.wort

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
    
    def setSpanisch(self, spanisch):
        self.spanisch = spanisch

    def getWort(self):
        return self.wort

    def getArtikel(self):
        return self.artikel

    def getSpanisch(self):
        return self.spanisch

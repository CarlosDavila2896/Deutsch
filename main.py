from wort import Wort
import random

JUGAR = 1
AGREGAR_PALABRAS = 2

global f
global m
global wortList

def main():
    global m
    while True:
        print("\n*****Menu*****")
        print("1. Jugar")
        print("2. Agregar palabras")
        print("3. Salir")
        m = int(input("Seleccione una: "))
        if(m > 0 and m < 4):
            break
    
    
     
    if(m == 3):
        print("Tschüs!!!")
        return

    cargarPalabras()    
    if(m == 1):
        juego()
        main()

    if(m == 2):
        agregarPalabras()
        main()


def cargarPalabras():
    global wortList
    global f
    wortList = []
    with open('wortebuch.txt', "r", encoding='utf-8') as f:
        for line in f:
            if len(line) > 1:
                artikel = line.split()[0]
                wort = line.split()[1]
                w = Wort(artikel,wort)
                wortList += [w]

    if m == AGREGAR_PALABRAS:
        f = open("wortebuch.txt", "a", encoding='utf-8')


def agregarPalabras():
    global f
    global wortList
    while True:
        wort = input("Ingrese una palabra: ")
        if(wort == "0"):
            f.close()
            return
        while True:
            artikel = input("Ingrese su articulo: ")
            if(artikel == "0"):
                f.close()
                return
            w = Wort(artikel,wort)
            if(w.checkArtikel()):
                break
            else:
                print("Artículo no valido")
        if (not w in wortList):
            f.write(str(w)+"\n")
        else:
            print("Esa palabra ya existe!")


def juego():
    global wortList
    while True:        
        aux = random.randrange(0,len(wortList))
        w = wortList[aux]
        resp = input("Cual es el articulo de " + w.getWort() + ": ")
        if(resp == "0"):
            return
        if(resp == w.getArtikel()):
            print("Richtig!!")
        else:
            print("Nein! El artículo correcto es: " + w.getArtikel())
        

if __name__ == "__main__":
    main()

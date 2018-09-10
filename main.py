# coding=utf-8

from wort import Wort
import random, case

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
                spanisch = line.split()[2]
                w = Wort(artikel,wort,spanisch)
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
        spanisch = input("Ingrese su traduccion al español: ")
        if(spanisch == "0"):
            f.close()
            return
        w.setSpanisch(spanisch)
        if (not w in wortList):
            f.write(str(w)+"\n")
        else:
            print("Esa palabra ya existe!")


def juego():
    global wortList
    while True:    
        d = bool(random.getrandbits(1))
        c = random.randint(0, 2)
        i = random.randrange(0,len(wortList))
        w = wortList[i]
        resp = input("Cual es el articulo de " + w.getWort() + " en " + case.traducir(c) + " (" + traducirDefinido(d) + ") : ")
        if(resp == "0"):
            return
        if(w.checkArtikelGame(resp, d, c)):
            print("Richtig!! Spanisch: " + w.getSpanisch())
        else:
            print("Nein! El artículo correcto es: " + w.getArtikel(c,d) + ". Spanisch: " + w.getSpanisch())
        print("")

def traducirDefinido(defined):
    if(defined):
        return 'definido'
    else:
        return 'indefinido'        

if __name__ == "__main__":
    main()

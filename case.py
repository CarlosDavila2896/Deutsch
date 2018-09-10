# coding=utf-8

NOMINATIV = 0
AKKUSATIV = 1
DATIV = 2

def traducir(case):
    if(case==NOMINATIV):
        return 'Nominativ'
    if(case==AKKUSATIV):
        return 'Akkusativ'
    if(case==DATIV):
        return 'Dativ'
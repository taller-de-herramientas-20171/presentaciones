#!/usr/bin/python3
import random


def dame_cadena():
    l = ['A', 'C', 'G', 'T']
    n = int(random.random() * 10)
    cadena = ''
    for i in range(n):
        pos = int(random.random() * len(l))
        cadena = cadena + l[pos]
    return cadena


def cuenta_subcadena(cadena, subcadena):
    if len(subcadena) > len(cadena):
        return None
    else:
        contador = 0
        for i in range(len(cadena)):
            if (i + len(subcadena)) > (len(cadena) - 1):
                return contador
            sub = cadena[i:(i + len(subcadena))]
            if sub == subcadena:
                contador += 1
        return contador

if __name__ == '__main__':
    adn = dame_cadena()
    subcadena = 'AT'
    total = cuenta_subcadena(adn, subcadena)
    print('ADN: ' + adn)
    print('La cadena: ' + subcadena + ' aparece ' + str(total) + ' veces')

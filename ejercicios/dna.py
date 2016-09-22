#!/usr/bin/python3
import random


def dame_cadena():
    """Genera una cadena de ADN de tamaño aleatorio.

    El tamaño de esta cadena puede estar entre 1 y 100 y esta
    constituida por las cuatro bases hidrogenadas:

    - A : Adenina
    - C : Citosina
    - G : Guanina
    - T : Timina"""
    l = ['A', 'C', 'G', 'T']
    n = int(random.random() * 100)
    cadena = ''
    for i in range(n):
        pos = int(random.random() * len(l))
        cadena = cadena + l[pos]
    return cadena


def cuenta_subcadena(cadena, subcadena):
    """Cuenta el número de veces que aparece la subcadena SUBCADENA
    dentro de la cadena CADENA.

    Por ejemplo:

    La cadena 'AT' aparece 3 veces en la cadena 'CATGGATCTTAT'

    Modo de uso:

    >>> conteo = cuenta_subcadena('CATGGATCTTAT', 'AT')
    >>> print('El número de veces que parece AT en CATGGATCTTAT es ' +
              str(conteo))
    >>> El número de veces que parece AT en CATGGATCTTAT es 3"""
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

#!/usr/bin/python3


def lee_archivo(archivo):
    f = open(archivo, 'r')
    return f.readlines()


def procesa_datos(datos):
    L = []
    for dato in datos:
        inf = dato.split()
        x = float(inf[0][inf[0].find("=") + 1:])
        y = float(inf[1][inf[1].find("=") + 1:])
        z = float(inf[2][inf[2].find("=") + 1:])
        tupla = (x, y, z)
        L.append(tupla)
    return L

datos = lee_archivo('datos.dat')
print(procesa_datos(datos))

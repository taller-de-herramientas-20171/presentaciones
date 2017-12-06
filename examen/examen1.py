#!/usr/bin/python3


def lee_archivo(archivo):
    return open(archivo, 'r').read().lower()


def primera_letra_frecuencias(archivo):
    datos = lee_archivo(archivo).split('\n')
    info = [(l[0], float(l[2:])) for l in datos if l != '']
    info.sort(key=lambda t: t[1], reverse=True)
    return info[0][0]


def encuentra_desplazamiento(arch_mensaje, arch_frec):
    mensaje = lee_archivo(arch_mensaje)
    d = {c: mensaje.count(c) for c in mensaje if letra_valida(c)}
    l = list(d.items())
    l.sort(key=lambda t: t[1], reverse=True)
    return ord(l[0][0]) - ord(primera_letra_frecuencias(arch_frec))


def letra_valida(c):
    return c not in (' ', '\n', 'ó', ',', 'í', '')


def descifra(mensaje, desplazamiento):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    mensaje = [abc[(abc.index(c) - d) % 26]
               if letra_valida(c) else c for c in mensaje]
    return ''.join(mensaje)


if __name__ == '__main__':
    m = lee_archivo('textoCifrado.txt')
    d = encuentra_desplazamiento('textoCifrado.txt', 'frecuencias.txt')
    print(descifra(m, d))

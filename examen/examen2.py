#!/usr/bin/python3


def lee_archivo(archivo):
    arch = open(archivo, 'r')
    datos = arch.read()
    datos = datos.lower()
    return datos


def primera_letra_frecuencias(archivo):
    datos = lee_archivo(archivo)
    datos = datos.split('\n')
    info = []
    for linea in datos:
        if linea != '':
            letra = linea.split()[0]
            frecuencia = float(linea.split()[1])
            tupla = (letra, frecuencia)
            info.append(tupla)
    info.sort(key=lambda tupla: tupla[1], reverse=True)
    primer_tupla = info[0]
    primer_letra = primer_tupla[0]
    return primer_letra


def encuentra_desplazamiento(archivo_mensaje, archivo_frecuencias):
    mensaje = lee_archivo(archivo_mensaje)
    frecuencias = {}
    for c in mensaje:
        if letra_valida(c):
            if c not in frecuencias:
                frecuencias[c] = 1
            else:
                frecuencias[c] += 1
    lista_tuplas = list(frecuencias.items())
    lista_tuplas.sort(key=lambda t: t[1], reverse=True)
    primer_tupla = lista_tuplas[0]
    primer_letra = primer_tupla[0]
    primer_letra_frecuencias = primera_letra_frecuencias(archivo_frecuencias)
    return ord(primer_letra) - ord(primer_letra_frecuencias)


def letra_valida(c):
    valido = c != ' ' and c != '\n' and c != 'ó' and c != 'í' and c != ',' and c != ''
    return valido


def descifra(mensaje, desplazamiento):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    mensaje_descifrado = ''
    for c in mensaje:
        if letra_valida(c):
            index_c = abecedario.index(c)
            nuevo_index_c = (index_c - desplazamiento) % 26
            nuevo_c = abecedario[nuevo_index_c]
            mensaje_descifrado += nuevo_c
        else:
            mensaje_descifrado += c
    return mensaje_descifrado


if __name__ == '__main__':
    m = lee_archivo('textoCifrado.txt')
    d = encuentra_desplazamiento('textoCifrado.txt', 'frecuencias.txt')
    print(descifra(m, d))

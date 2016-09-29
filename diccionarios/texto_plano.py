# !/usr/bin/python3

from urllib.request import Request, urlopen
from pprint import pprint


def obten_archivo(url, nombre_archivo):
    """Dada la url URL, obtiene la información de esa página web y la
    guarda en el archivo NOMBRE_ARCHIVO.

    Después devuelve el archivo para futuras manipulaciones."""
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read().decode('utf-8')
    archivo = open(nombre_archivo, 'w')
    archivo.write(webpage)
    archivo.close()
    archivo = open(nombre_archivo, 'r')
    return archivo


def guarda_archivo(archivo):
    """Cierra el archivo ARCHIVO para que ya no pueda ser
    modificado."""
    archivo.close()


def procesa_archivo_clima(archivo):
    """Se encarga de generar un diccionario a partir del archivo
    ARCHIVO. Este diccionario tiene la siguiente estructura:

    d = {2016: {1: {'air frost': 5.0,
               'rain': 83.9,
               'sun': 59.1,
               'tmax': 9.4,
               'tmin': 3.0},
           2: {'air frost': 5.0,
               'rain': 46.7,
               'sun': 104.1,
               'tmax': 9.1,
               'tmin': 2.9},
           3: {'air frost': 5.0,
               'rain': 74.2,
               'sun': 123.8,
               'tmax': 10.2,
               'tmin': 2.1},
           4: {'air frost': 1.0,
               'rain': 49.9,
               'sun': 157.9,
               'tmax': 13.3,
               'tmin': 4.2},
           5: {'air frost': 0.0,
               'rain': 86.1,
               'sun': 202.9,
               'tmax': 18.3,
               'tmin': 8.8},
           6: {'air frost': 0.0,
               'rain': 75.9,
               'sun': 106.2,
               'tmax': 19.9,
               'tmin': 12.2},
           7: {'air frost': 0.0,
               'rain': 14.1,
               'sun': 190.2,
               'tmax': 22.8,
               'tmin': 13.5},
           8: {'air frost': 0.0,
               'rain': 45.8,
               'sun': 207.9,
               'tmax': 23.1,
               'tmin': 13.7}}},
    'location': 'Location: 450900E 207200N, Lat 51.761 Lon -1.262, 63
    metres amsl',
    'place': 'Oxford'}"""
    datos = {}
    datos['place'] = archivo.readline().strip()
    datos['location'] = archivo.readline().strip()
    for i in range(5):
        archivo.readline()
    datos['data'] = {}
    for linea in archivo:
        columnas = linea.split()
        año = int(columnas[0])
        mes = int(columnas[1])
        if columnas[-1] == 'Provisional':
            del columnas[-1]
        for i in range(2, len(columnas)):
            if columnas[i] == '---':
                columnas[i] = None
            elif columnas[i][-1] == '*' or columnas[i][-1] == '#':
                # Strip off trailing character
                columnas[i] = float(columnas[i][:-1])
            else:
                columnas[i] = float(columnas[i])
        tmax, tmin, air_frost, rain, sun = columnas[2:]
        if not año in datos['data']:
            datos['data'][año] = {}
        datos['data'][año][mes] = {'tmax': tmax,
                                   'tmin': tmin,
                                   'air frost': air_frost,
                                   'sun': sun,
                                   'rain': rain}
    return datos


def obten_info_sol(datos):
    """Obtiene una lista de listas de los promedios de las horas
    soleadas entre 1929 y 2010"""
    sun = [[datos['data'][y][m]['sun'] for m in range(1, 13)]
           for y in range(1929, 2010)]
    return sun

if __name__ == '__main__':
    url = 'http://www.metoffice.gov.uk/climate/uk/stationdata/oxforddata.txt'
    print('Descargando desde: {}'.format(url))
    archivo = obten_archivo(url, '/tmp/datos.txt')
    print('Archivo descargado {}'.format(archivo.name))
    print('Iniciando procesamiento')
    datos = procesa_archivo_clima(archivo)
    pprint(datos)
    guarda_archivo(archivo)
    print('Obteniendo información de porcentajes solares')
    sol = obten_info_sol(datos)
    pprint(sol)
    print('Terminando de procesar\nGuardando archivo')

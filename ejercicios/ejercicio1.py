#!/usr/bin/python3

# -*- encoding: utf-8 -*-

# Creamos nuestras variables de conversión

METRO = 1
PULGADA = 0.0254
METRO_A_PULGADAS = METRO / PULGADA
PIE = 12 * PULGADA
METRO_A_PIES = METRO / PIE
YARDA = 3 * PIE
METRO_A_YARDAS = METRO / YARDA
MILLA = 1760 * YARDA
METRO_A_MILLAS = METRO / MILLA

# Imprimimos los valores de conversión. También podemos calcular cosas
# dentro de las llamadas a funciones.

print('640 metros corresponden a {:6.4f} pulgadas'
      .format(640 * METRO_A_PULGADAS))
print("640 metros corresponden a {:6.4f} pies".format(640 * METRO_A_PIES))
print("640 metros corresponden a {:6.4f} yardas".format(640 * METRO_A_YARDAS))
print("640 metros corresponden a {:6.4f} millas".format(640 * METRO_A_MILLAS))

# En python3, la notación '{}'.format(val) es la nueva aceptada dentro
# del lenguaje, la cuál entra en sustitución de la notación
# '%f'%(val). Más información en https://pyformat.info/

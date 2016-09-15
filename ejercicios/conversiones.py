# Hacer un programa en el dada una determinada longitud en metros, 
# calcular y escribir la longitud correspondiente medido en pulgadas, en pies, en yardas, y en millas. 

# Una pulgada es 2.54 cm.

# Un pie es de 12 pulgadas

# Una yarda es 3 pies

# Una milla es de 1760 yardas. 

# Para la verificacion: una longitud de 640 metros corresponde a 25196.85 pulgadas, 2099.74 pies, 699.91 yardas, o 0.3977 millas.


inch = 0.0254  # Converted to meters
foot = inch * 12
yard = foot * 3
mile = yard * 1760

# Test
metres = 640.0

inches = metres / inch
feet = metres / foot
yards = metres / yard
miles = metres / mile

print("{m:g} metres is equivalent to {i:g} inches, {f:g} feet, {y:g} yards, {mi:g} miles.".format(m=metres, i=inches, f=feet, y=yards, mi=miles))



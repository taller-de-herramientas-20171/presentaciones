import sympy as sy


# Resuelve la ecuacion: (7x + 3 (x + 1) + 1) * 2 = 0

# 1. Define la ecuacion usando sympy.

# 2. Diferenciar la expresion en 1) una y dos veces.
# Ahora define y_2 que es la expresion integrada de la primera derivada

# 3. Encuentra las raices: los valores de la ecuacion cuando es igual a 0. Inserta las raices para verificar los resultados.

# Imprime todos los valores.


x = sy.symbols("x")
y = (((7 * x + 3 * (x+1)) + 1) * 4) - (2 * x)

print("Equation: ", y)

dydx = sy.diff(y, x)
print("First Derivade: ", dydx)

ddydx = sy.diff(dydx, x)
print("Second Derivade: ", ddydx)

roots = sy.solve(y, x)
print("Roots of the equation: ", roots)

s = y.subs(x, roots[0])
print("Subtitution of roots: ", s)

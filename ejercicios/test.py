# Escribe una funcion que calcule la suma:
# \[ s= \sum_{k=1}^M \frac{3k}{k^3+1} \]

# Escribe otra funcion test-sum que compruebe la funcion anterior y verifique que el resultado sea correcto.

# Esta funcion converge a 3.334

# Para ello determina a partir de que valor de M, la funcion converge con un margen de error chico.

# Esta funcion debera decir si la funcion paso la prueba o no.


def s(m):
    s = 0
    for k in range(1,(m+1)):
        s += (3.0 * k) / (k ** 3 + 1)
    return s


def test_sum():
    epsilon_error = 0.01
    convergence_value = 3.334
    m = 500

    for i in range(1, m):
        obtained_value = s(i)
        if convergence_value - obtained_value < epsilon_error:
            print("First Convergence Value: ", i)
            return True
    return False


print(test_sum())

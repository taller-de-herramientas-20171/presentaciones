# Supongamos que p es la tasa de interes de un banco en tanto por ciento por anio.
# Una cantidad inicial A ha crecido a

# \[ A (1 + \frac{p}{100})^n \]

# despues de n anios.

# Hacer un programa para el calculo de la cantidad de dinero de 1000 euros 
# que ha crecido despues de 3 anios con una tasa de interes del 5 por ciento.


interest_rate = 5.0  # in percent
years = 3
initial_amount = 1000
# Calculate final amount due to interest rate
final_amount = initial_amount * (1 + interest_rate / 100) ** years
print final_amount

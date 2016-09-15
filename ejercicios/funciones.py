# * Planea tu viaje
# 1. Define una funcion llamada *hotel-cost* que recibe *noches* como entrada.

# 2. El hotel cuesta $140 por noche. Por lo tanto, la funcion hotel-cost debe regresar 140 * noches.

# 3. Define una funcion llamada *extras* que recibe un entero como entrada que es la cantidad de gastos extras por dia y el numero de noches de viaje.

# 4. Define una funcion trip-cost que tome dos argumentos, extras y noches. La funcion debe regresar la suma de llamar a las funciones  hotel-cost(noches), y extras(extra).



def hotel_cost(nights):
   return 140 * nights

def extras(extra, nights):
   money = extra * nights
   return money


def trip_cost(extra, nights):
    return hotel_cost(nights) + extras(extra, nights)

extra = 50
nights = 10
total = trip_cost(extra, nights)
print("Trip cost for ", nights, " nights and ", extra, " extras expenses per day is: ", total)




# * Calcula los impuestos y propina de tu comida
# - Dado el costo de tu comida, crea funciones que:
#   - Calcule los impuesto de tu comida. Agrege el 8% a la cuenta total.
#   - Calcule la propina de tu comida. 15%

# - Imprima el costo total de tu comida con impuestos y el total con propina.

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print("With tax: %0.2f" % bill)
    return bill


def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print("With tip: %0.2f" % bill)
    return bill
    
meal_cost = 100
print("Meal cost: ", meal_cost)
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

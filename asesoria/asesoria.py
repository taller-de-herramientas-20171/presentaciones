# saliendo de un ciclo
for i in range(10):
    if i == 2:
        print('es par')
        break
    print(i)


def imprime():
    print('Hola mundo')


def abre():
    print('abriendo archivo')


def menu():
    print('Bienvenido a mi menu\n')
    while True:
        print('Selecciona un opción\n')
        print('1.- Imprime hola\n')
        print('2.- Abre archivo\n')
        print('0.- Salir\n')
        opcion = int(input())
        if opcion == 0:
            break
        elif opcion == 1:
            imprime()
        elif opcion == 2:
            abre()
        else:
            print('Opción incorrecta')

if __name__ == '__main__':
    menu()

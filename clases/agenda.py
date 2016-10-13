#!/usr/bin/python3

###########################################################
# Implementación del proyecto de la agenda usando clases. #
# Autor: Miguel Angel Piña Avelino                        #
# Materia: Taller de herramientas computacionales.        #
# Facultad de Ciencias, UNAM                              #
###########################################################


from datetime import datetime
from functools import reduce


class Persona(object):
    """Representa una persona. Este objeto va a tener los siguientes
    atributos:
    * Nombre
    * Fecha de nacimiento
    * Correo electrónico
    * Teléfono"""

    def __init__(self, nombre, fecha_nac, correo, telefono):
        """Constructor de la clase. Espera recibir los siguientes
        atributos como cadenas:
        * nombre: Nombre de la persona
        * fecha_nac: Cadena con la fecha de nacimiento de la
          persona. Esta cadena debe tener la siguiente estructura
          dd/mm/YYYY.
        * correo: Correo electrónico.
        * telefono: Teléfono de la persona."""
        self.nombre = nombre
        self.fecha_nac = datetime.strptime(fecha_nac, "%d/%m/%Y")
        self.correo = correo
        self.telefono = telefono

    def imprime_persona(self):
        """Imprime los atributos de una persona."""
        print(
            "Nombre: {} \nEdad: {}\nFecha de nacimiento: {}\nTelefono: {}\nCorreo {}".format(
                self.nombre,
                self.edad(),
                self.fecha_nac,
                self.telefono,
                self.correo))

    def edad(self):
        "Regresa la edad de la persona en años."
        hoy = datetime.today()
        return hoy.year - self.fecha_nac.year - \
            ((hoy.month, hoy.day) < (self.fecha_nac.month, self.fecha_nac.day))


class Agenda(object):
    """Clase que se encarga de modelar una agenda. Esta clase tiene
    definidas las siguientes funciones:

    * agrega(persona)
    * busca(nombre_o_telefono)
    * elimina(nombre_o_telefono)
    * imprime-agenda()
    * actualiza(nombre_o_telefono, persona)
    * contacto_mayor()
    * contacto_menor()
    * promedio()"""

    def __init__(self):
        """Constructor de la clase agenda. Inicializa una lista vacía
        que servirá para almacenar las personas."""
        self.lista = []

    def agrega(self, persona):
        """Agrega una persona a la agenda."""
        self.lista.append(persona)

    def busca(self, nom_or_tel):
        """Busca una persona en la agenda, utilizando el nombre o el
        telefono."""
        for persona in self.lista:
            if persona.nombre == nom_or_tel or persona.telefono == nom_or_tel:
                return persona

    def elimina(self, nom_or_tel):
        """Elimina una persona buscándola a través del nombre o el
        número de teléfono."""
        self.lista.remove(self.busca(nom_or_tel))

    def imprime_agenda(self):
        """Imprime las personas registradas en la agenda."""
        for persona in self.lista:
            persona.imprime_persona()
            print("****************************")

    def actualiza(self, nom_or_tel, persona):
        """Se encarga de actualizar una persona buscándola a través de
        su nombre o número de telefono. Para hacer la actualización es
        necesario construir un objeto de tipo Persona que remplazará
        al objecto indicado."""
        for i, p in enumerate(self.lista):
            if p.nombre == nom_or_tel or p.telefono == nom_or_tel:
                self.lista.pop(i)
                self.lista.insert(i, persona)

    def contacto_mayor(self):
        """Regresa la persona con mayor edad dentro de la agenda."""
        contacto_mayor = None
        for persona in self.lista:
            if contacto_mayor is None:
                contacto_mayor = persona
            elif contacto_mayor.fecha_nac < persona.fecha_nac:
                contacto_mayor = persona
        return contacto_mayor

    def contacto_menor(self):
        """Regresa la persona con menor edad dentro de la agenda."""
        contacto_menor = None
        for persona in self.lista:
            if contacto_menor is None:
                contacto_menor = persona
            elif contacto_menor.fecha_nac > persona.fecha_nac:
                contacto_menor = persona
        return contacto_menor

    def promedio(self):
        """Cálcula el promedio de la edad de las personas dentro de la
        agenda."""
        suma_persona = lambda p1, p2: float(p1.edad() + p2.edad())
        if len(self.lista) < 2:
            if len(self.lista) == 0:
                promedio = 0.
            else:
                promedio = float(self.lista[0].edad())
        else:
            promedio = reduce(suma_persona, self.lista) / len(self.lista)
        print("El promedio de edad es: {}".format(promedio))


def lee_opcion():
    """Intenta leer una opción hasta que ingresen un valor de tipo
    numérico."""
    while True:
        try:
            return int(input())
        except:
            print("Lo que ingresaste no fue un número. Intenta nuevamente.")


class Menu(object):
    """Representa un menú."""

    def __init__(self):
        """Inicializa la agenda."""
        self.agenda = Agenda()

    def menu(self):
        """Muestra el menú con las operaciones que están permitidas
        dentro de la agenda."""
        while True:
            print("Bienvenido\n")
            print("Por favor selecciona una opción")
            print("1) Agregar una persona")
            print("2) Borrar una persona")
            print("3) Actualizar una persona")
            print("4) Buscar un contacto")
            print("5) Recuperar el contacto más grande")
            print("6) Recuperar el contacto más chico")
            print("7) Imprimir el promedio de edad")
            print("8) Imprimir la agenda")
            print("0) Salir")
            opcion = lee_opcion()
            if opcion == 1:
                self.__agregar()
            elif opcion == 2:
                self.__borrar()
            elif opcion == 3:
                self.__actualiza()
            elif opcion == 4:
                self.__busca()
            elif opcion == 5:
                self.__contacto_mayor()
            elif opcion == 6:
                self.__contacto_menor()
            elif opcion == 7:
                self.__promedio()
            elif opcion == 8:
                self.__imprime()
            elif opcion == 0:
                break
            else:
                print("Opción incorrecta, intenta nuevamente")

    def __agregar(self):
        print("\n==================================\n")
        nombre = input("Dame el nombre: ")
        telefono = input("Dame el telefono: ")
        fecha_nac = input("Dame la fecha de nacimiento (dd/mm/YYYY): ")
        correo = input("Dame el correo: ")
        persona = Persona(nombre, fecha_nac, correo, telefono)
        self.agenda.agrega(persona)
        print("\n==================================\n")

    def __borrar(self):
        print("\n==================================\n")
        nom_or_tel = input("Dame el nombre o número de teléfono: ")
        self.agenda.elimina(nom_or_tel)
        print("Eliminado")
        print("\n==================================\n")

    def __actualiza(self):
        print("\n==================================\n")
        nom_or_tel = input(
            "Dame el nombre o número de teléfono del contacto a actualizar: ")
        p = self.agenda.busca(nom_or_tel)
        correo = input("Dame el nuevo correo: ")
        fecha_nac = input("Dame la nueva fecha de nacimiento (dd/mm/YYYY): ")
        p.correo = correo
        p.fecha_nac = fecha_nac
        self.agenda.actualiza(nom_or_tel, p)
        print("\n==================================\n")

    def __busca(self):
        print("\n==================================\n")
        nom_or_tel = input(
            "Dame el nombre o número de teléfono del contacto a buscar: ")
        p = self.agenda.busca(nom_or_tel)
        print("\n==================================\n")
        p.imprime_persona()
        print("\n==================================\n")

    def __contacto_mayor(self):
        print("\n==================================\n")
        p = self.agenda.contacto_mayor()
        p.imprime_persona()
        print("\n==================================\n")

    def __contacto_menor(self):
        print("\n==================================\n")
        p = self.agenda.contacto_menor()
        p.imprime_persona()
        print("\n==================================\n")

    def __promedio(self):
        print("\n==================================\n")
        self.agenda.promedio()
        print("\n==================================\n")

    def __imprime(self):
        print("\n==================================\n")
        self.agenda.imprime_agenda()
        print("\n==================================\n")

if __name__ == '__main__':
    menu = Menu()
    menu.menu()

# gestor.py

import pickle
import os

ARCHIVO = "actividad2/personajes.pckl"

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        # Validar que el nombre sea una cadena no vacía
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía")

        # Validar que vida, ataque, defensa y alcance sean enteros mayores que cero
        if not isinstance(vida, int) or vida <= 0:
            raise ValueError("Vida debe ser un entero mayor que cero")
        if not isinstance(ataque, int) or ataque <= 0:
            raise ValueError("Ataque debe ser un entero mayor que cero")
        if not isinstance(defensa, int) or defensa <= 0:
            raise ValueError("Defensa debe ser un entero mayor que cero")
        if not isinstance(alcance, int) or alcance <= 0:
            raise ValueError("Alcance debe ser un entero mayor que cero")

        self.nombre = nombre.strip()
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance


class Gestor:
    def __init__(self):
        # Diccionario donde se guardan los personajes usando el nombre como clave
        self.personajes = {}
        self.cargar()

    def cargar(self):
        # Si el fichero existe, se cargan los personajes guardados
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, "rb") as fichero:
                self.personajes = pickle.load(fichero)

    def guardar(self):
        # Guarda el diccionario de personajes en el fichero binario
        with open(ARCHIVO, "wb") as fichero:
            pickle.dump(self.personajes, fichero)

    def agregar(self, personaje):
        # Si el personaje ya existe, no se añade
        if personaje.nombre in self.personajes:
            print("El personaje", personaje.nombre, "ya existe. No se añadió.")
        else:
            self.personajes[personaje.nombre] = personaje
            self.guardar()
            print("Personaje", personaje.nombre, "añadido.")

    def mostrar(self):
        # Muestra todos los personajes guardados
        if len(self.personajes) == 0:
            print("No hay personajes en el gestor.")
        else:
            print("Personajes:")
            for p in self.personajes.values():
                print(" -", p.nombre, "| Vida:", p.vida, "| Ataque:", p.ataque,
                      "| Defensa:", p.defensa, "| Alcance:", p.alcance)

    def borrar(self, nombre):
        # Borra un personaje a partir de su nombre
        if nombre in self.personajes:
            del self.personajes[nombre]
            self.guardar()
            print("Personaje", nombre, "borrado.")
        else:
            print("No existe el personaje", nombre)

# Crear el gestor
gestor = Gestor()

# Crear los tres personajes de la tabla
caballero = Personaje("Caballero", 4, 2, 4, 2)
guerrero = Personaje("Guerrero", 2, 4, 2, 4)
arquero = Personaje("Arquero", 2, 4, 1, 8)

# Añadirlos al gestor
gestor.agregar(caballero)
gestor.agregar(guerrero)
gestor.agregar(arquero)

# Mostrar los personajes
print("Personajes después de agregar:")
gestor.mostrar()

# Borrar al Arquero
gestor.borrar("Arquero")

# Mostrar de nuevo el gestor
print("Personajes después de borrar a Arquero:")
gestor.mostrar()
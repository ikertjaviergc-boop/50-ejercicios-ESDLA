# ==========================================
# NIVEL 3: LA COMPAÑÍA (POO)
# ==========================================

import random

# Ejercicio 27 & 28 — La Clase Personaje y Constructor de Elrond
class Personaje:
    total_creados = 0 # Ejercicio 38: Atributo de clase

    def __init__(self, nombre, raza, edad, vida=100):
        # Validaciones del constructor
        self.nombre = nombre if nombre.strip() != "" else "Desconocido"
        self.raza = raza
        self.edad = edad if edad >= 0 else 0
        self.vida = min(100, max(0, vida))
        self.arma = None # Ejercicio 29
        Personaje.total_creados += 1

    def presentarse(self):
        return f"Soy {self.nombre}, un {self.raza} de {self.edad} años."

    def recibir_dano(self, cantidad):
        self.vida = max(0, self.vida - cantidad)

    def esta_vivo(self):
        return self.vida > 0

    def equipar_arma(self, arma):
        self.arma = arma

    def atacar(self, objetivo):
        if self.arma:
            dano = self.arma.dano
            print(f"{self.nombre} ataca a {objetivo.nombre} con {self.arma.nombre} infligiendo {dano} de daño.")
            objetivo.recibir_dano(dano)
        else:
            print(f"{self.nombre} ataca con los puños infligiendo 5 de daño.")
            objetivo.recibir_dano(5)

    def __str__(self):
        return f"[{self.raza}] {self.nombre} | Edad: {self.edad} | Vida: {self.vida}/100"

    @classmethod
    def censo(cls):
        print(f"Censo Total de la Tierra Media: {cls.total_creados} personajes creados.")

# Ejercicio 29 — El Arma Legendaria
class Arma:
    def __init__(self, nombre, dano, material):
        self.nombre = nombre
        self.dano = dano
        self.material = material

    def describir(self):
        return f"Arma: {self.nombre} ({self.material}) - Daño: {self.dano}"

# Ejercicio 30 — Las Razas de la Tierra Media
class Hobbit(Personaje):
    def __init__(self, nombre, edad, comidas_al_dia=7):
        super().__init__(nombre, "Hobbit", edad)
        self.comidas_al_dia = comidas_al_dia

    def segundo_desayuno(self):
        self.vida = min(100, self.vida + 10)
        print(f"{self.nombre} ha tomado su segundo desayuno (+10 vida).")

    def presentarse(self): # Ejercicio 32
        return f"Soy {self.nombre} y me gustan las fiestas y el buen tabaco."

class Elfo(Personaje):
    def __init__(self, nombre, edad, punteria=100):
        super().__init__(nombre, "Elfo", edad)
        self.punteria = punteria

    def disparar_flecha(self, objetivo):
        print(f"{self.nombre} dispara una flecha precisa a {objetivo.nombre}.")
        objetivo.recibir_dano(25)

    def presentarse(self): # Ejercicio 32
        return f"Soy {self.nombre}, mi vista alcanza más allá del horizonte."

class Enano(Personaje):
    def __init__(self, nombre, edad, resistencia_barba=50):
        super().__init__(nombre, "Enano", edad)
        self.resistencia_barba = resistencia_barba

    def golpe_de_hacha(self, objetivo):
        print(f"{self.nombre} asesta un potente hachazo a {objetivo.nombre}.")
        objetivo.recibir_dano(30)

    def presentarse(self): # Ejercicio 32
        return f"¡Soy {self.nombre}! Y no me llames pequeño."

# Ejercicio 31 — El Mago Blanco
class Mago(Personaje):
    def __init__(self, nombre, edad, color="Gris", mana=100):
        super().__init__(nombre, "Mago", edad)
        self.color = color
        self.mana = mana

    def lanzar_hechizo(self, nombre_hechizo, costo):
        if self.mana >= costo:
            self.mana -= costo
            print(f"{self.nombre} lanza {nombre_hechizo} (Maná restante: {self.mana}).")
        else:
            print("Maná insuficiente.")

    def ascender(self):
        if self.color.lower() == "gris":
            self.color = "Blanco"
            self.mana = 200
            print(f"{self.nombre} ha ascendido a Mago Blanco!")

# Ejercicio 33 — La Compañía como Objeto
class Compania:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregar_miembro(self, personaje):
        if len(self.miembros) < 9:
            self.miembros.append(personaje)
            print(f"{personaje.nombre} se ha unido a {self.nombre}.")
        else:
            print("La Compañía ya tiene 9 miembros.")

    def eliminar_miembro(self, nombre):
        self.miembros = [m for m in self.miembros if m.nombre != nombre]

    def listar_miembros(self):
        print(f"=== {self.nombre} ===")
        for m in self.miembros:
            print(m)

    def total_vida(self):
        return sum(m.vida for m in self.miembros)

# Ejercicio 34 — El Anillo Único (Encapsulamiento)
class AnilloUnico:
    def __init__(self, portador_inicial):
        self.__portador_actual = portador_inicial
        self.__nivel_corrupcion = 0

    def cambiar_portador(self, nuevo_portador):
        self.__portador_actual = nuevo_portador
        self.__nivel_corrupcion += 10
        print(f"El Anillo pasa a {nuevo_portador}. Corrupción: {self.__nivel_corrupcion}")
        if self.__nivel_corrupcion >= 100:
            print("El portador se ha convertido en Gollum.")

    def get_corrupcion(self):
        return self.__nivel_corrupcion

# Ejercicio 35 — La Batalla del Abismo de Helm
class Guerrero(Personaje): pass
class Orco(Personaje): pass

def simular_batalla(g1, g2):
    print(f"\n--- BATALLA: {g1.nombre} vs {g2.nombre} ---")
    turno = 1
    while g1.esta_vivo() and g2.esta_vivo():
        print(f"Turno {turno}:")
        g1.atacar(g2)
        if g2.esta_vivo():
            g2.atacar(g1)
        turno += 1
    ganador = g1 if g1.esta_vivo() else g2
    print(f"¡Ganador de la batalla: {ganador.nombre}!\n")

# Ejercicio 36 — El Ejército de Mordor (Composición)
class Ejercito:
    def __init__(self):
        self.orcos = []

    def reclutar(self, orco):
        self.orcos.append(orco)

    def bajas(self):
        return sum(1 for o in self.orcos if not o.esta_vivo())

    def fuerza_total(self):
        return sum(o.arma.dano if o.arma else 5 for o in self.orcos if o.esta_vivo())

    def atacar_fortaleza(self, resistencia):
        fuerza = self.fuerza_total()
        print(f"Fuerza del ejército: {fuerza} vs Resistencia: {resistencia}")
        return fuerza > resistencia

# Ejercicio 37 — Los Nazgûl (Herencia Múltiple / Multinivel)
class Humano(Personaje): pass
class Rey(Humano): pass
class Nazgul(Rey):
    def grito_aterrador(self, lista_objetivos):
        print("¡El Rey Brujo emite un grito aterrador!")
        for p in lista_objetivos:
            p.recibir_dano(15)

# Pruebas integradas Nivel 3
aragorn = Guerrero("Aragorn", "Humano", 87)
anduril = Arma("Andúril", 35, "Acero")
aragorn.equipar_arma(anduril)

orco_feo = Orco("Uruk-hai", "Orco", 10, vida=60)
simular_batalla(aragorn, orco_feo)

# Ejercicio 38 & 39 — Demostración de Censo e Integración
Personaje.censo()
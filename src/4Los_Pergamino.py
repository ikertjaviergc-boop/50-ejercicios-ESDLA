# ==========================================
# NIVEL 4: LOS PERGAMINOS (Diccionarios y Regex)
# ==========================================

import re

# Ejercicio 40 — El Diccionario de la Compañía
compania_dict = {
    "Frodo": "Hobbit",
    "Legolas": "Elfo",
    "Gimli": "Enano",
    "Aragorn": "Humano"
}
print("Claves:", list(compania_dict.keys()))
print("Valores:", list(compania_dict.values()))
compania_dict["Boromir"] = "Humano"
del compania_dict["Boromir"] # Eliminado de la lista
print("¿Sauron está en el diccionario?:", "Sauron" in compania_dict, "\n")

# Ejercicio 41 — La Ficha Completa
personajes_nest = {
    "Aragorn": {"raza": "Humano", "edad": 87, "arma": "Andúril", "vida": 100},
    "Legolas": {"raza": "Elfo", "edad": 2931, "arma": "Arco", "vida": 100},
}
print("Edad de Legolas:", personajes_nest["Legolas"]["edad"])
personajes_nest["Aragorn"]["arma"] = "Espada de Montaraz"

for nombre, datos in personajes_nest.items():
    print(f"Ficha de {nombre}: {datos}")
print()

# Ejercicio 42 — El Contador de Palabras del Libro Rojo
texto_libro = "Un anillo para gobernarlos a todos un anillo para encontrarlos un anillo para atraerlos a todos y en las tinieblas atarlos"
palabras = texto_libro.lower().split()
conteo_palabras = {}
for p in palabras:
    conteo_palabras[p] = conteo_palabras.get(p, 0) + 1

ordenadas = sorted(conteo_palabras.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 palabras más repetidas:", ordenadas, "\n")

# Ejercicio 43 — El Inventario del Reino
armeria = {"espadas": 340, "arcos": 120, "hachas": 87, "lanzas": 200}

def agregar_arma(nombre, cantidad):
    armeria[nombre] = armeria.get(nombre, 0) + cantidad

def usar_arma(nombre, cantidad):
    if armeria.get(nombre, 0) >= cantidad:
        armeria[nombre] -= cantidad

def stock_total():
    return sum(armeria.values())

def arma_mas_abundante():
    return max(armeria, key=armeria.get)

print("Stock total armería:", stock_total())
print("Arma más abundante:", arma_mas_abundante(), "\n")

# Ejercicio 44 — El Registro de Batallas por Reino
batallas = {
    "Gondor": [340, 120, 87],
    "Rohan": [500, 210],
    "Mordor": [1200, 890, 450, 300]
}

max_bajas = 0
reino_mas_afectado = ""

for reino, lista_bajas in batallas.items():
    total_b = sum(lista_bajas)
    prom_b = total_b / len(lista_bajas)
    print(f"Reino: {reino} | Total bajas: {total_b} | Promedio: {prom_b:.2f} | Batallas: {len(lista_bajas)}")
    if total_b > max_bajas:
        max_bajas = total_b
        reino_mas_afectado = reino

print(f"Reino con más bajas: {reino_mas_afectado} ({max_bajas})\n")

# Ejercicio 45 — El Validador de Nombres Élficos (regex)
import re

def validar_nombre_elfico(nombre):
    patron = r"^[A-ZÁÉÍÓÚÄËÏÖÜ][a-záéíóúäëïöü]{3,14}$"
    return bool(re.match(patron, nombre))

nombres_test = ["Galadriel", "legolas", "Ar", "Elrond99", "Nínuiel"]
for n in nombres_test:
    print(f"Nombre '{n}': Valido -> {validar_nombre_elfico(n)}")
print()

# Ejercicio 46 — El Descifrador de Runas
mensaje = "El ejercito de 340 orcos partio el 03/12/3019 desde la Torre 7 hacia Minas Tirith con 12 trolls"
numeros = re.findall(r"\d+", mensaje)
fechas = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", mensaje)
mayusculas = re.findall(r"\b[A-Z][a-z]*\b", mensaje)

print("Números hallados:", numeros)
print("Fechas halladas:", fechas)
print("Palabras con mayúscula:", mayusculas, "\n")

# Ejercicio 47 — Los Mensajeros de Gondor
datos = ["aragorn@gondor.me", "gandalf_gris@istari", "legolas@bosquenegro.elf", "+56 9 8765 4321", "12345"]
patron_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
patron_fono = r"^\+56\s9\s\d{4}\s\d{4}$"

for item in datos:
    if re.match(patron_email, item):
        print(f"'{item}' -> Email Válido")
    elif re.match(patron_fono, item):
        print(f"'{item}' -> Teléfono Chileno Válido")
    else:
        print(f"'{item}' -> Formato Inválido")
print()

# Ejercicio 48 — La Censura de Mordor
texto_mordor = "Sauron observa. Sauron espera. El poder de Sauron crece cada dia."
censurado_todo = re.sub(r"Sauron", "[EL INNOMBRABLE]", texto_mordor)
conteo_sauron = len(re.findall(r"Sauron", texto_mordor))
censurado_dos = re.sub(r"Sauron", "[EL INNOMBRABLE]", texto_mordor, count=2)

print("Censura Total:", censurado_todo)
print("Apariciones de Sauron:", conteo_sauron)
print("Censura Parcial (2 primeras):", censurado_dos, "\n")

# Ejercicio 49 — El Parser del Pergamino Antiguo
pergamino = """nombre:Frodo|raza:Hobbit|edad:33|arma:Dardo
nombre:Legolas|raza:Elfo|edad:2931|arma:Arco
nombre:Gimli|raza:Enano|edad:139|arma:Hacha"""

lista_personajes_parsed = []
for linea in pergamino.strip().split("\n"):
    dic_p = {}
    items = linea.split("|")
    for item in items:
        k, v = item.split(":")
        dic_p[k] = v
    lista_personajes_parsed.append(dic_p)

print("Tabla de personajes procesada:")
for p in lista_personajes_parsed:
    print(f"- {p['nombre']} ({p['raza']}), Edad: {p['edad']}, Arma: {p['arma']}")
print()

# Ejercicio 50 — 🏆 El Concilio Final (Proyecto Integrador)
class SistemaTierraMedia:
    def __init__(self):
        self.db_personajes = {}

    def menu(self):
        print("=== SISTEMA DE LA TIERRA MEDIA ===")
        print("1. Registrar personaje")
        print("2. Listar todos los personajes")
        print("3. Buscar personaje (regex)")
        print("4. Simular batalla")
        print("5. Ver estadísticas")
        print("0. Salir")

    def ejecutar_demostración(self):
        print("Cargando datos predeterminados en el Concilio Final...")
        self.db_personajes["Frodo"] = {"raza": "Hobbit", "edad": 33, "vida": 100}
        self.db_personajes["Aragorn"] = {"raza": "Humano", "edad": 87, "vida": 100}
        print("Sistema iniciado con éxito. El Concilio está preparado.")

sistema = SistemaTierraMedia()
sistema.ejecutar_demostración()
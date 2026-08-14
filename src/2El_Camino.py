# ==========================================
# NIVEL 2: EL CAMINO
# ==========================================

# Ejercicio 14 — La Compañía del Anillo
# Operaciones de indexación, slicing y reversión de listas
compania = ["Frodo", "Sam", "Merry", "Pippin", "Aragorn", "Gandalf", "Legolas", "Gimli", "Boromir"]
print("Compañía completa:", compania)
print("Cantidad de miembros:", len(compania))
print("Primero y Último:", compania[0], "|", compania[-1])
print("Los 4 Hobbits:", compania[0:4])
print("Lista invertida:", compania[::-1], "\n")

# Ejercicio 15 — El Registro de Batallas
# Definición de función receptora e impresión de formato
def registrar_batalla(nombre, orcos_derrotados):
    print(f"{nombre} derrotó a {orcos_derrotados} orcos.")

registrar_batalla("Aragorn", 87)
registrar_batalla("Legolas", 92)
registrar_batalla("Gimli", 91)
registrar_batalla("Boromir", 40)
registrar_batalla("Faramir", 25)
print()

# Ejercicio 16 — La Calculadora de Elrond
# Función con fórmula de daño ajustada para evitar valores negativos
def calcular_dano(ataque, defensa):
    dano = (ataque * 2) - defensa
    return max(0, dano)

print("Daño test 1:", calcular_dano(50, 30))
print("Daño test 2 (defensa alta):", calcular_dano(10, 50), "\n")

# Ejercicio 17 — Contador de Pasos de Sam
# Iteración secuencial con acumulación
total_acumulado = 0
for dia in range(1, 11):
    total_acumulado += 27
    print(f"Día {dia}: 27 km (Total: {total_acumulado} km)")
print()

# Ejercicio 18 — Las Escaleras de Cirith Ungol
# Ciclo while simulando ascenso de escalones
escalon = 0
while escalon <= 20:
    if escalon > 0 and escalon % 5 == 0 and escalon != 20:
        print(f"Frodo descansa en el escalón {escalon}")
    escalon += 1
print("Has llegado a la cima.\n")

# Ejercicio 19 — El Inventario de Bilbo
# Métodos de inserción, remoción y ordenamiento de listas
inventario = []
inventario.extend(["Dardo", "Cota de mithril", "Anillo Único", "Pipa", "Mapa"])
inventario.remove("Anillo Único")
inventario.insert(0, "Libro rojo")

print("¿Dardo está en el inventario?:", "Dardo" in inventario)
inventario.sort()
print("Inventario ordenado:", inventario, "\n")

# Ejercicio 20 — El Ejército de Rohan
# Procesamiento de arreglos sin usar funciones integradas (max, min, sum)
tropas = [120, 340, 87, 500, 210, 65, 430]

total_soldados = 0
max_tropas = tropas[0]
idx_max = 0
min_tropas = tropas[0]

for idx, cantidad in enumerate(tropas):
    total_soldados += cantidad
    if cantidad > max_tropas:
        max_tropas = cantidad
        idx_max = idx
    if cantidad < min_tropas:
        min_tropas = cantidad

promedio_tropas = total_soldados / len(tropas)
print(f"Total soldados: {total_soldados}")
print(f"Aldea con más tropas: {max_tropas} (Índice {idx_max})")
print(f"Aldea con menos tropas: {min_tropas}")
print(f"Promedio por aldea: {promedio_tropas:.2f}\n")

# Ejercicio 21 — El Filtro de Gandalf
# Separación de datos mediante listas y tuplas
def filtrar_aliados(personajes):
    aliados = []
    enemigos = []
    for nombre, es_aliado in personajes:
        if es_aliado:
            aliados.append(nombre)
        else:
            enemigos.append(nombre)
    return aliados, enemigos

lista_p = [("Legolas", True), ("Saruman", False), ("Éowyn", True), ("Grima", False)]
aliados_list, enemigos_list = filtrar_aliados(lista_p)
print("Aliados:", aliados_list)
print("Enemigos:", enemigos_list, "\n")

# Ejercicio 22 — Las Rimas del Anillo
# Recorrido e inspección de strings
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    conteo = {v: 0 for v in "aeiou"}
    total = 0
    for char in texto.lower():
        if char in conteo:
            conteo[char] += 1
            total += 1
    return total, conteo

frase = "Un anillo para gobernarlos a todos"
total_v, desglose = contar_vocales(frase)
print(f"Frase: '{frase}'")
print(f"Total vocales: {total_v}")
print(f"Desglose por vocal: {desglose}\n")

# Ejercicio 23 — La Torre de Orthanc
# Construcción geométrica con ciclos anidados
def dibujar_torre(n):
    print(f"Torre de Orthanc (altura {n}):")
    for i in range(n):
        espacios = " " * (n - i - 1)
        asteriscos = "*" * (2 * i + 1)
        print(espacios + asteriscos)

dibujar_torre(5)
print()

# Ejercicio 24 — El Menú de la Posada del Póney Pisador
# Estructura interactiva basada en bucle de control
def menu_posada_simulado():
    lista_personajes = ["Barliman"]
    opcion = "1" # Simulación para la prueba
    if opcion == "1":
        print("Personajes en la posada:", lista_personajes)

menu_posada_simulado()
print()

# Ejercicio 25 — El Buscador de Moria
# Algoritmo manual de búsqueda secuencial
def buscar_personaje(lista, nombre_buscado):
    for i in range(len(lista)):
        if lista[i] == nombre_buscado:
            return i
    return -1

print("Índice de Gimli:", buscar_personaje(compania, "Gimli"))
print("Índice de Sauron:", buscar_personaje(compania, "Sauron"), "\n")

# Ejercicio 26 — Los Números de la Suerte de Gollum
# Implementación de algoritmos numéricos clásicos
def es_par(n):
    return n % 2 == 0

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def es_primo(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def fibonacci(n):
    if n <= 0: return []
    if n == 1: return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

n_test = 10
print(f"Resultados para n = {n_test}:")
print(f"Es par: {es_par(n_test)}")
print(f"Factorial: {factorial(n_test)}")
print(f"Es primo: {es_primo(n_test)}")
print(f"Fibonacci ({n_test}): {fibonacci(n_test)}\n")
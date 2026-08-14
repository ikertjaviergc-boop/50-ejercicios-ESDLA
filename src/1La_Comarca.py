# ==========================================
# NIVEL 1: LA COMARCA
# ==========================================

# Ejercicio 01 — El Censo de Bolsón Cerrado
# Definición de variables con los datos de Frodo y despliegue con f-string
nombre = "Frodo Bolsón"
edad = 33
estatura_cm = 106.7
es_portador_del_anillo = True
raza = "Hobbit"

print("=== FICHA DE PERSONAJE ===")
print(f"Nombre: {nombre}")
print(f"Raza: {raza}")
print(f"Edad: {edad} años")
print(f"Estatura: {estatura_cm} cm")
print(f"Portador del Anillo: {es_portador_del_anillo}\n")

# Ejercicio 02 — Las Constantes de la Tierra Media
# Definición de constantes en mayúsculas y cálculo de porcentajes
ANILLOS_ELFOS = 3
ANILLOS_ENANOS = 7
ANILLOS_HOMBRES = 9
ANILLO_UNICO = 1

total_anillos = ANILLOS_ELFOS + ANILLOS_ENANOS + ANILLOS_HOMBRES + ANILLO_UNICO
print(f"Total de Anillos de Poder: {total_anillos}")
print(f"Porcentaje Elfos: {(ANILLOS_ELFOS / total_anillos) * 100:.2f}%")
print(f"Porcentaje Enanos: {(ANILLOS_ENANOS / total_anillos) * 100:.2f}%")
print(f"Porcentaje Hombres: {(ANILLOS_HOMBRES / total_anillos) * 100:.2f}%")
print(f"Porcentaje Anillo Único: {(ANILLO_UNICO / total_anillos) * 100:.2f}%\n")

# Ejercicio 03 — La Vara de Medir de Gandalf
# Cálculos de diferencias, proporciones y conversiones de unidades
gandalf_m = 1.78
gimli_m = 1.37

dif_cm = (gandalf_m - gimli_m) * 100
proporcion = gandalf_m / gimli_m
promedio_m = (gandalf_m + gimli_m) / 2
gandalf_pulgadas = (gandalf_m * 100) / 2.54

print(f"Diferencia: {dif_cm:.2f} cm")
print(f"Gimli cabe {proporcion:.2f} veces en Gandalf")
print(f"Estatura promedio: {promedio_m:.2f} m")
print(f"Gandalf en pulgadas: {gandalf_pulgadas:.2f} in\n")

# Ejercicio 04 — El Peso del Anillo
# Cálculo del peso percibido y acumulado por fatiga
peso_real = 0.03
peso_percibido = peso_real * 1000
dias = 180
fatiga_diaria = 0.5
peso_total_acumulado = peso_real + (dias * fatiga_diaria)

# El número 1024 (2**10) es fundamental en informática porque representa 1 Kilobyte (2^10 bytes) en sistema binario.
potencia_base_dos = 2 ** 10

print(f"Peso percibido: {peso_percibido} kg")
print(f"Peso acumulado a 180 días: {peso_total_acumulado} kg")
print(f"2^10 = {potencia_base_dos} (Representa la base del sistema binario/bytes)\n")

# Ejercicio 05 — El Segundo Desayuno
# Operaciones aritméticas, división entera y residuo
COMIDAS_DIARIAS = 7
COSTO_COMIDA = 1250

gasto_diario = COMIDAS_DIARIAS * COSTO_COMIDA
gasto_semanal = gasto_diario * 7
gasto_anual = gasto_diario * 365

presupuesto = 500000
dias_completos = presupuesto // gasto_diario
dinero_sobrante = presupuesto % gasto_diario

print(f"Gasto diario: {gasto_diario} monedas")
print(f"Gasto semanal: {gasto_semanal} monedas")
print(f"Gasto anual: {gasto_anual} monedas")
print(f"Días completos de comida con 500,000 monedas: {dias_completos}")
print(f"Dinero sobrante: {dinero_sobrante} monedas\n")

# Ejercicio 06 — ¿Eres digno de portar el Anillo?
# Evaluación de rangos de edad con condicionales
def evaluar_edad_personaje(nombre_p, edad_p):
    if edad_p < 33:
        return f"{nombre_p}: Eres demasiado joven, la mayoría de edad hobbit es 33."
    elif 33 <= edad_p <= 100:
        return f"{nombre_p}: Puedes unirte a la Compañía."
    elif 101 <= edad_p <= 500:
        return f"{nombre_p}: Eres sabio, serás consejero."
    else:
        return f"{nombre_p}: Eres un Maia o un Elfo. Lidera el Concilio."

print(evaluar_edad_personaje("Pippin", 28))
print(evaluar_edad_personaje("Frodo", 50))
print(evaluar_edad_personaje("Elrond", 1500) + "\n")

# Ejercicio 07 — La Balanza de Mithril
# Comparaciones relacionales directas
VALOR_MITHRIL = 1_000_000
VALOR_COMARCA = 850_000

print(f"¿El mithril vale más que la Comarca? {VALOR_MITHRIL > VALOR_COMARCA}")
print(f"¿El mithril vale menos que la Comarca? {VALOR_MITHRIL < VALOR_COMARCA}")
print(f"¿Valen exactamente lo mismo? {VALOR_MITHRIL == VALOR_COMARCA}")
print(f"¿Tienen valores distintos? {VALOR_MITHRIL != VALOR_COMARCA}\n")

# Ejercicio 08 — El Concilio de Elrond
# Evaluación lógica con and, or, not
def puede_entrar(edad_p, usa_arma, usa_magia, es_orco):
    return (edad_p > 18) and (usa_arma or usa_magia) and (not es_orco)

print(f"Aragorn entra: {puede_entrar(87, True, False, False)}")
print(f"Gandalf entra: {puede_entrar(2000, False, True, False)}")
print(f"Orco entra: {puede_entrar(30, True, False, True)}\n")

# Ejercicio 09 — El Ojo de Sauron
# Evaluación de detección del Ojo con tabla de verdad
def verificar_ojo(anillo_puesto, distancia_km):
    if anillo_puesto and distancia_km < 100:
        return "⚠️ SAURON TE HA VISTO"
    return "Estás a salvo... por ahora."

casos = [
    (True, 45),
    (True, 150),
    (False, 30),
    (False, 200)
]

for ap, dist in casos:
    print(f"Anillo: {ap}, Distancia: {dist}km -> {verificar_ojo(ap, dist)}")
print()

# Ejercicio 10 — El Clima de Caradhras
# Control de flujo según rangos de temperatura
def clima_caradhras(temp):
    if temp > 15:
        return "Clima agradable, la Compañía avanza rápido."
    elif 0 <= temp <= 15:
        return "Hace frío, abriguen a los hobbits."
    elif -20 <= temp < 0:
        return "Ventisca. Saruman está atacando la montaña."
    else:
        return "Imposible cruzar. Vayan por las Minas de Moria."

print(f"Temperatura 18°C: {clima_caradhras(18)}")
print(f"Temperatura -5°C: {clima_caradhras(-5)}")
print(f"Temperatura -25°C: {clima_caradhras(-25)}\n")

# Ejercicio 11 — El Salario de un Montaraz
# Cálculo de tarifa de pago según orcos derrotados y escala de bonos
def calcular_pago_montaraz(orcos):
    PAGO_POR_ORCO = 35000
    pago_base = orcos * PAGO_POR_ORCO
    bono_porcentaje = 0
    
    if orcos > 100:
        bono_porcentaje = 0.35
    elif orcos > 50:
        bono_porcentaje = 0.20
        
    bono = pago_base * bono_porcentaje
    total = pago_base + bono
    return pago_base, bono, total

base, bono, total = calcular_pago_montaraz(60)
print(f"Orcos: 60 -> Base: {base}, Bono: {bono}, Total: {total}\n")

# Ejercicio 12 — Conversor de Distancias de la Tierra Media
# Conversión de unidades y análisis temporal de marcha
def convertir_distancia_leguas(leguas):
    km = leguas * 4.828
    m = km * 1000
    dias_hobbit = km / 30
    dias_caballo = km / 90
    
    print(f"Leguas: {leguas} -> {km:.2f} km | {m:.2f} m")
    print(f"Días Hobbit: {dias_hobbit:.1f} | Días Caballo: {dias_caballo:.1f}")
    if dias_hobbit > 30:
        print("Necesitarás las Águilas.")

convertir_distancia_leguas(200)
print()

# Ejercicio 13 — El Verificador de Palantír
# Lógica XOR para interacción con el Palantír
def probar_palantir(voluntad_fuerte, sangre_real):
    if voluntad_fuerte and sangre_real:
        return "Dominas el Palantír por completo."
    elif voluntad_fuerte ^ sangre_real:
        return "Puedes ver visiones, pero corres peligro."
    else:
        return "Sauron te corrompe."

combinaciones = [(True, True), (True, False), (False, True), (False, False)]
for v, s in combinaciones:
    print(f"Voluntad: {v}, Sangre Real: {s} -> {probar_palantir(v, s)}")
print()
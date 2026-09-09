# ============================================================
# ENTRADA DE VARIABLES
# ============================================================

print("ejercicio 1")
print("="* 30)

num_galletas = int(input(("Cuantas galletas quieres? : ")))
costo = float(input("cual es el costo de las galletas? : "))
dinero = float(input(("Cuanto dinero tienes? : ")))
cant_dinero = num_galletas * costo
galletas = dinero // costo

print(f"Para esa cantidad de galletas necesitas {cant_dinero}")
print(f"tienes {dinero},te alcanza para {galletas} galletas\n\n")


# Ejercicio 2: Área de un rectángulo
base   = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

area = base * altura   # fórmula: base × altura

print(f"El área del rectángulo es: {area}")


# Ejercicio 3: Conversión de minutos a horas y minutos
minutos_totales = int(input("\n\nIngrese la cantidad de minutos: "))

horas   = minutos_totales // 60   # división entera → horas completas
minutos = minutos_totales % 60    # módulo → minutos restantes

print(f"{minutos_totales} minutos equivalen a esta cantidad de horas: {horas} y minutos: {minutos} \n\n")


# Ejercicio 4: Cálculo del precio con descuento
precio    = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: \nEjemplo 50% = 50\n"))

valor_descuento = precio * (descuento / 100)   # valor que se descuenta
precio_final    = precio - valor_descuento      # precio con descuento

print(f"El precio final con ese descuento es: {precio_final}\n\n")


# Ejercicio 5: Intercambio de valores entre dos variables
a = float(input("Ingrese el valor de la variable a: "))
b = float(input("Ingrese el valor de b: "))

auxiliar = a   # guardar temporalmente el valor de a
a = b          # a toma el valor de b
b = auxiliar   # b toma el valor original de a

print(f"Los valores originales son: a = {a} y b= {b}\nDespués del intercambio: a = {a} , b = {b}\n\n")




##########################################################################################################
#       Taller tema 1
#        A partir de los ejemplos resueltos anteriormente, resolver en Python los siguientes 5 ejercicios. 
#        Todos los ejercicios deben solicitar los datos necesarios al usuario mediante input(), 
#        mostrar los resultados con print() y estar comentados.
###########################################################################################################

# 1. solicitar el ancho y el largo de un un terreno rectangular y calcular su perimetro

lado = float(input("Para este terreno cual es su ancho? "))
lado2 = float(input("Para este terreno cual es su largo? "))
perimetro = 2*lado2+2*lado
print(f"El perimetro del campo con {lado} y {lado2} son {perimetro} metros\n\n")


# 2. solicitar tres numeros y dar su promedio
nun1,num2,num3 = float(input("dame tres numeros: ")), float(input("el segundo numero: ")), float(input("el tercero numero: "))
prom = (num2+num3+nun1)/3
print(f"El promedio de {nun1}, {num2}, {num3} es: {prom}\n\n")


# 3. Solicitar el nombre yla edad de una persona y mostrar un mensaje de presentacion
nombre,edad = input("Cual es tu nombre?: "), float(input("cual es tu edad? :"))
print(f"hola {nombre} veo que tienes {edad} años\n\n")

# 4. solicitar un valor en pesos comerciales y mostra los pesos en dolares a 1usd=3100cop
dinero1 = float(input("cuanto dinero colombiano vas a cambiar a USD?\n\n"))
usd  = dinero1/3100
print(f"Ahora tienes {usd} en dolares")

# 5. Solicitar una cantidad de segundos y convertirla a horas, minutos y segundos.


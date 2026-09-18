#############################   ciclo for   ##############################
# Ejercicio 1: Mostrar la tabla de multiplicar de un número
#

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):          # recorre los valores del 1 al 10
    print(f"{numero} x {i} = {numero * i}")
    

# Ejercicio 2: Sumar los primeros n números naturales
n = int(input("Ingrese un número entero positivo: "))

suma = 0        #contador para almacenar la suma de los números naturales
for i in range(1, n + 1):
    suma = suma + i

print(f"La suma de los primeros {n} números naturales es: {suma}")


# Ejercicio 3: Contar cuántos números pares hay entre 1 y n
n = int(input("Ingrese un número entero positivo: "))

contador = 0
numero   = 1
while numero <= n:
    if numero % 2 == 0:
        contador = contador + 1
    numero = numero + 1

print(f"Hay {contador} números pares entre 1 y {n}")
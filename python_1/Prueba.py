
segundos_totales = int(input("El valor que coloques los pasara a horas minutos y segundos\nCuantos segundos quieres trasformar?   \n\n"))

# Cálculos
horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos_restantes = segundos_totales % 60

print(f"\nLos {segundos_totales} segundos son en horas: {horas}\nen minutos son: {minutos} minutos\ny {segundos_restantes} segundos")
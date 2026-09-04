# Creacion de variables #
nombre = "alex"         #Var tipo string#
documento = 13233       #Var tipo entero#
direccion = "calle 21"  #var tipo string#
tiene_deuda= False      #var tipo Bool#

print(nombre)           #mostrar en pantalla#

print(" Concatenacion usando +")
print( "=" * 30)

#forma de unir varibles, usando el simb, +, pero todos deben ser STR#
print(" Mi nombre es "+ nombre + " y mi documento es "+ str(documento))

#Opcion 2, agregando variables con coma#
print("Mi nombre es ",nombre," y mi documento es",documento," y mi dirreccion es ",direccion)

#Opcion 3, con f#
print(f"Hola mi nombre es {nombre} y vivo en {direccion} y mi estado actual de deudas es {tiene_deuda}")

#uso de las tres commilas en  print#
print(f"""
Hola mi nombre es {nombre}
mi direccion es {direccion}
mi estado de deuda es {tiene_deuda}
""")

#Saltos de linea con barra invertida \#
print(f"Hola mi nombre es {nombre}\ny mi documento es {documento}")


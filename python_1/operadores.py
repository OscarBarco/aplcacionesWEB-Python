# ============================================================
# OPERADORES ARITMÉTICOS EN PYTHON
# ============================================================

numero1 = 7
numero2 = 2

suma     = numero1 + numero2
resta    = numero1 - numero2
multip   = numero1 * numero2
division = numero1 / numero2
div_ent  = numero1 // numero2
residuo  = numero1 % numero2
potencia = numero1 ** numero2

print(f"""
Resultado de Operaciones Aritméticas:
suma:            {numero1} +  {numero2} = {suma}
resta:           {numero1} -  {numero2} = {resta}
multiplicacion:  {numero1} *  {numero2} = {multip}
division:        {numero1} /  {numero2} = {division:.4f}
division_entera: {numero1} // {numero2} = {div_ent}
residuo:         {numero1} %  {numero2} = {residuo}
potencia:        {numero1} ** {numero2} = {potencia}
""")




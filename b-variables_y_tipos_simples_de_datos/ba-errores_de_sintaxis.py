# No se puede usar una apóstrofe(') en este caso
mensaje = 'Una apóstrofre(')'

# El error producido es:

# File "ba-errores_de_sintaxis.py", line 2
#     mensaje = 'Una apóstrofre(')'
#                                ^
# SyntaxError: invalid syntax

# Que signfica un error de sintaxis en la segunda línea

# Soluciones (comentar la segunda línea antes de usar):
mensaje = 'Una apóstrofe(\')'
print(mensaje)

mensaje = "Una apóstrofe(')"
print(mensaje)

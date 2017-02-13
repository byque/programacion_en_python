edad = 24
mensaje = "¡Feliz cumpleaños número " + edad + "!"

print(mensaje)

# Produce el siguiente error:
# Traceback (most recent call last):
#   File "be-imprimir_numeros_con_error.py", line 2, in <module>
#     mensaje = "¡Feliz cumpleaños número " + edad + "!"
# TypeError: Can't convert 'int' object to str implicitly

# Este es un error de tipografía porque Python no puede reconocer el tipo de
# información que se está usando (¿string o int?)

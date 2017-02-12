# Espacio al final de la cadena
lenguaje = 'python '
print(lenguaje + "<-Aquí está el espacio")

# Quitar temporalmente el espacio al final
print(lenguaje.rstrip() + "<-Espacio removido temporalmente")

# La variable original no ha cambiado
print(lenguaje + "<-Aquí está de nuevo el espacio")

# Quitar permanentemente el espacio al final
lenguaje = lenguaje.rstrip()
print(lenguaje + "<-Espacio removido permanentemente")

# Espacio al inicio y al final de la cadena
lenguaje = ' python '
print("Espacio al inicio y al final:->" + lenguaje + "<-")

# Quitar temporalmente el espacio del principio
print("Quitar espacio del incio:->" + lenguaje.lstrip() + "<-")

# Quitar temporalmente ambos espacios
print("Quitar ambos espacios:->" + lenguaje.strip() + "<-")

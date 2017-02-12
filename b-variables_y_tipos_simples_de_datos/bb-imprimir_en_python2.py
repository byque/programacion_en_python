# Imprimir en python 2 es un poco diferente
mensaje = "Hola mundo Python 2!"
print mensaje

print "Impresion en Python 2"

# En la versión 2
# mensaje = "¡Hola mundo Python 2!"

# Produce el error:
# File "bb-imprimir_en_python2.py", line 2
# SyntaxError: Non-ASCII character '\xc2' in file bb-imprimir_en_python2.py on line 2, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

# Por los símbolos adicionales del español (¡, ñ, á,ó,é,ú, etc)
# se recomienda Python 3 para los principiantes hispanohablantes

# Usar context managers para apertura de archivos o conecciones a bases de datos, lo cual nos evita tener que 
# preocuparnos por cerrar las conecciones después de usar los recursos

# Caso típico:
f = open('archivo.txt', 'r')
contenido = f.read()
# si no necesito volver a usar el archivo, ya lo cierro y libero recursos
f.close()

palabras = contenido.split(' ')
cantidad_palabras = len(palabras)

print(cantidad_palabras)

# Versión usando context manager
with open('archivo.txt', 'r') as f:
    contenido = f.read()
# NOTA: ver que no hace falta cerrar el archivo en forma explícita

palabras = contenido.split(' ')
cantidad_palabras = len(palabras)

print(cantidad_palabras)

print(cantidad_palabras+5)

print('Cantidad de palabras + 7: ',cantidad_palabras+7)

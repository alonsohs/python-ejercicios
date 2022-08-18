# l2= []
# n = int(input("Cuantos numeros vas a ingresar? \n"))

# for i in range(n):
#     dato = int(input("Introduce el valor {0}: \n".format(i+1)))
#     l2.append(dato)

# print(l2)

# for i in range(len(l2)):
#     print(l2[i])

# generos = ('Masculino', 'Femenino', 'otro')
# print(generos)
# lista = list(generos)
# lista.append('Otro mas')
# generos = tuple(lista)
# print(generos)

alum = {
    1: 'Alonso',
    2: 'Valeria',
    3: 'Ximena',
    4: 'Omar'
}

print(list(alum.keys()))

alum['5'] = 'Javier'
alum.setdefault(1, 'Nuevo')

for key, value in alum.items():
    print("{0}: {1}".format(key, value))


# Tarea, crear un programa en python que permita decalrar un dict vacio y permitirle al usuario agregar n elementos
# Modificar el valor de una clave especifica
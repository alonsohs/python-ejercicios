dictionary = {}
n = int(input("Cuantas entradas vas a ingresar? \n"))

for i in range(n):
    clave = input("Introduce la clave para la entrada {0}: \n".format(i+1))
    valor = input("Introduce la valor para la entrada {0}: \n".format(i+1))
    dictionary.setdefault(clave, valor)

print("\nDiccionario resultante\n")

for key, value in dictionary.items():
    print("- {0}: {1}".format(key, value))

editarValor = True
haCambiadoUnValor = False
while editarValor:
    seguir = int(input("\nQuiere modificar algun valor? 1(si) 0(no) \n"))
    if seguir == 1:
        clave = input("Introduce la clave que quieres modificar: \n")
        if clave in dictionary.keys():
            nuevoValor = input("Introduce el nuevo valor para '{0}': \n".format(clave))
            dictionary[clave] = nuevoValor
            haCambiadoUnValor = True
        else:
            print("La clave que ingresó no existe, intente de nuevo.")
    else:
        editarValor = False

if haCambiadoUnValor:
    print("\nDiccionario resultante\n")
    for key, value in dictionary.items():
        print("- {0}: {1}".format(key, value))

# Definir el abecedario sin Ñ explícitamente
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Pedir clave (desplazamiento)
clave = int(input("Ingrese la clave (número de desplazamiento): "))

# Pedir palabra
palabra = input("Ingrese una palabra: ").upper()

resultado = ""

for letra in palabra:
    if letra in abecedario:
        # Encontrar la posición actual de la letra
        indice = abecedario.index(letra)
        # Calcular nueva posición con desplazamiento
        nuevo_indice = (indice + clave) % len(abecedario)
        # Añadir la nueva letra al resultado
        resultado += abecedario[nuevo_indice]
    else:
        # Si no está en el abecedario (espacios, símbolos, etc.)
        resultado += letra

print("Palabra cifrada:", resultado)



#creame la sintaxis de python en donde esté la variable clave, que la tenga que escribir desde teclado el usuario.luego, quiero que se pida dictar una palabra, para posteriormente aplicar el desplazamiento. para ello, utiliza un arreglo que tenga el abcdario, para guiarte en los desplazamientos, que se recorra este abcedario la cantidad necesaria para elegir la nueva letra. no tomes en cuenta la Ñ. POR EJEMPLO, si la letra es A y el desplazamiento es 3, la nueva letra tiene que ser D
	

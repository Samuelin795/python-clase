numeros = [(input ("Ingrese numeros: ") for _ in range(8))]

for i in range(len (numeros)):
    for j in range(0, len(numeros) -i -1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

repetidos = {}
for numero in numeros:
    for numero in repetidos:
        numeros 
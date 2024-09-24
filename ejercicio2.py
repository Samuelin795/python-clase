numeros = [(input(f"ingresa numeros: " )) for _ in range(8)]

for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Los datos ingresados: " 'numeros')
repetidos = {}
for numero in numeros:
    if numero in repetidos:
        repetidos[numero] += 1
    else:
        repetidos[numero] = 1

print("Numeros repetido mas de 2 veces es: ")
for numero, conteo in repetidos.items():
    if conteo > 1:
        print(numero)
num = int(input('Ingrese Cantidad de numeros: '))
while num < 4:
    num = int(input('Ingrese Cantidad de numeros: '))

lista = []
for x in range(0,num):
    string = 'Ingrese un numero entre 4-6 digitos:'
    number = input(string)
    size = len(number)
    while size < 4 or size > 6:
        number = input(string)
        size = len(number)
    lista.append(number)

resultados = []
def sumaPar(n):
    suma = 0
    for character in n:
        # Converitmos cada caracter del string en entero 
        # para la suma
        num = int(character)
        suma = suma + num
    if suma % 2 == 0:
        resultados.append(int(n))

for x in lista:
    sumaPar(x)

print(resultados)

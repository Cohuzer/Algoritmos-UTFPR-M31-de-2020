# NÚMERO UM
print('NÚMERO 1)')
print('Número 1) a)')
for i in range(1, 101):
    print(i)

print('\nNúmero 1) b)')
for i in range(10, 51):
    if i%2 == 0:
        print(i)

print('\nNúmero 1) c)')
for i in range(20, -1, -1):
    print(i)


print('\nNúmero 1) d)')
soma = 0
for i in range(3, 11):
    soma += i
print(soma)

print('\nNúmero 1) e)')
soma = 0
for i in range(4, 21):
    if i%2 == 0:
        soma += i
print(soma)

print('\nNúmero 1) f)')
multiplicacao = 1
for i in range(2, 6):
    multiplicacao *= i
print(multiplicacao)

print('\nNúmero 1) g)')
soma = 0
qnt = 0
for i in range(10, 51):
    if i%2 != 0:
        soma += i
        qnt += 1
print(f'{soma/qnt}')

print('\nNúmero 1) h)')
soma = 0
qnt = 0
for i in range(10, 51):
    if i%5 == 0:
        soma += i
        qnt += 1
print(f'{soma/qnt}')

#NÚMERO DOIS
print('\nNÚMERO 2)')
numeros = [5, 13, 17, 29, 45, 78]
for i in range(0, len(numeros)):
    print(f'{numeros[i]} X 2 = {numeros[i]*2}')

#NÚMERO TRÊS
print('\nNÚMERO 3)')
numeros = list()
for i in range(0, 10):
    numeros.append(float(input(f'Digite o {i + 1}° número: ')))
print('\nRESPOSTAS 3)')
for i in range(0, len(numeros)):
    print(f'{numeros[i]} X 2 = {numeros[i]*2}')

#NÚMERO QUATRO
print('\nNÚEMRO 4)')
numeros = list()
soma = 0
for i in range(0, 5):
    numeros.append(float(input(f'Digite o {i + 1} número: ')))
print('\nRESPOSTAS 4)')
for i in range(0, len(numeros)):
    soma += numeros[i]
print(f'A média dos números da lista é {soma/len(numeros)}')

#NÚMERO CINCO)
print('\nNÚMERO 5)')
numeros = [11, 14, 29, 33, 42, 55, 68]
for i in range(0, len(numeros)):
    if numeros[i]%2 == 0:
        print(f'{numeros[i]} é PAR')
    else:
        print(f'{numeros[i]} é IMPAR')

#NÚMERO SEIS)
print('\nNÚMERO 6)')
numeros = [11, 14, 29, 33, 42, 55, 68]
par = list()
impar = list()
for i in range (0, len(numeros)):
    if numeros[i]%2 == 0:
        par.append(numeros[i])
    else:
        impar.append(numeros[i])
print(f'Número Pares = {par}\nNúmeros Impares = {impar}')

#NÚMERO SETE)
print('\nNÚMERO 7)')
numeros = list()
for i in range (0, 5):
    numeros.append(int(input(f'Digite o {i + 1}° valor inteiro: ')))

#LETRA A)
print(f'\nLetra A) {numeros[::-1]}')

#LETRA B)
print(f'\nLetra B) O maior valor é {max(numeros)}, e sua primeira aparição foi na posição {numeros.index(max(numeros))} do vetor')

#LETRA C)
print(f'\nLetra C) O menor valor é {min(numeros)}, e sua primeira aparição foi na posição {numeros.index(min(numeros))} do vetor')

#LETRA D)
print(f'\nLetra D)')

numeros2 = list()
for i in range(0, len(numeros)):
    numeros2.append(numeros[i])
#Essa lista de numeros2 serve para não mudar a lista original, preserva-la pra E

for i in range(0, len(numeros2)):
    if numeros2.count(numeros2[i]) != 1 and numeros2[i] != []:
        print(f'O número {numeros2[i]} se repete {numeros2.count(numeros2[i])} vezes')
        for c in range(0, numeros.count(numeros[i])):
            numeros2[numeros2.index(numeros[i])] = []
    elif numeros2[i] != []:
        print(f'O {i + 1}° valor não se repete')
#Diga se de passagem que eu achei muito lindo isso que eu fiz na D

#Letra E)
print(f'\nLetra E)')

numeros2 = list()
for i in range(0, len(numeros)):
    numeros2.append(numeros[i])
#Clonei a lista para evitar erros lógicos de novo

for i in range(0, len(numeros)):
    if numeros[i] != []:
        print(f'O número {numeros[i]} se repete {numeros.count(numeros[i])} vez(es)')
        for c in range(0, len(numeros)):
            if numeros2[i] == numeros[c]:
                numeros[c] = []

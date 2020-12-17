i = 0
numeros = list()
pares = list()
impares = list()
soma = 0

for i in range(0, 10):
    numeros.append(int(input(f'Insira o {i + 1}° número: ')))

for i in numeros:
    soma += i
    if i%2 == 0:
        pares.append(i)
    else:
        impares.append(i)


print(f'\033[1;33m\nNúmeros pares => {pares}\nNúmeros impares => {impares}')
print(f'A soma dos elementos é {soma}\nA média dos elementos é {soma/len(numeros):.2f}')
print(f'O menor valor digitado foi {min(numeros)} na posição {numeros.index(min(numeros))} da lista')

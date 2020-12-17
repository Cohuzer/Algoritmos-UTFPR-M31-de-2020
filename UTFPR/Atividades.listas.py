i = 0
lista = []
while i != 5:
    lista.append(float(input(f'Insira o {i + 1}° valor da lista: ')))
    i += 1
print(lista)

i = 0
lista2 = []
while i != 5:
    num = int(input(f'Insira o {i + 1}° valor a ser elevado ao quadrado: '))
    lista2.append(num*num)
    i += 1
print(lista2)

i = 0
lista3 = []
while i != 5:
    num = int(input(f'Insira o {i + 1}° valor a ser adicionado: '))
    if num > 0:
        lista3.append(num)
        i += 1
    else:
        print('\033[31m Opção invalida, tente novamente: \033[m')

matriz = [[], [], [], []]
for i in range(4):
    for j in range(4):
        matriz[i].append(int(input(f'Digite o valor para posição ({i}, {j}): ')))

print('\n')

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'[{matriz[i][j]: ^5}]', end='')
    print()

print('\n')

def Soma_Linha(Matriz):
    soma = maior = menor = posi_mai = posi_min = 0
    medias = []
    for i in range(len(Matriz)):
        soma = 0
        for j in range(len(Matriz[i])):
            soma += Matriz[i][j]
        soma /= len(Matriz[i])
        medias.append(soma)
    for i in range(len(medias)):
        if i == 0:
            maior = menor = medias[i]
            posi_mai = posi_min = i
        elif medias[i] > maior:
            maior = medias[i]
            posi_mai = i
        elif medias[i] < menor:
            menor = medias[i]
            posi_min = i
    print(f'A linha {posi_mai} tem a maior média, {maior:.2f}')
    print(f'A linha {posi_min} tem a menor média, {menor:.2f}')

def Soma_Coluna(Matriz):
    soma = maior = menor = posi_mai = posi_min = 0
    medias = []
    for j in range(len(Matriz)):
        soma = 0
        for i in range(len(Matriz[j])):
            soma += Matriz[i][j]
        soma /= len(Matriz[i])
        medias.append(soma)
    for i in range(len(medias)):
        if i == 0:
            maior = menor = medias[i]
            posi_mai = posi_min = i
        elif medias[i] > maior:
            maior = medias[i]
            posi_mai = i
        elif medias[i] < menor:
            menor = medias[i]
            posi_min = i
    print(f'A coluna {posi_mai} tem a maior média, {maior:.2f}')
    print(f'A coluna {posi_min} tem a menor média, {menor:.2f}')

Soma_Linha(matriz)
Soma_Coluna(matriz)

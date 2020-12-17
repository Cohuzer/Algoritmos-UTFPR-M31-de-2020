#Mapas/Dicionarios:
#Número 1)
Boletim = {}

def Nome_Dict(quantidade):
    escopo = list()
    escopo_nota = list()
    for i in range(quantidade):
        escopo.append(str(input(f'Nome do {i + 1}° aluno: ')))
        escopo_nota.append(float(input(f'Nota do {escopo[i]}: ')))
    for i in range(len(escopo)):
        Boletim[f'{escopo[i]}'] = escopo_nota[i]
    print()

quantidade = int(input('Quantos alunos serão catalogados? '))
Nome_Dict(quantidade)

for i in Boletim.keys():
    print(f'O aluno {i} tirou {Boletim[i]}')

#Número 2)

def Média(Dict):
    escopo = qnt = 0
    for i in Dict.keys():
        escopo += Dict[i]
        qnt += 1
    escopo /= qnt
    return escopo

print(f'\nA média entre os alunos foi: {Média(Boletim):.2f}\n')

#Número 3)

def Acima_Média(Dict):
    for i in Dict.keys():
        if Média(Dict) < Dict[i]:
            print(f'{i} tirou {Dict[i]}, ele esta acima da média')

Acima_Média(Boletim)

print('\033[1;31mMATRIZES\033[m\n')
#Número 1)
Matriz = [[], [], [], []]
print('Número 1)')
def Declara_Matriz(Matriz):
    tamanho = len(Matriz)
    for i in range(tamanho):
        for j in range(tamanho):    
            Matriz[i].append(int(input(f'Insira um valor para a coordenada [{i}, {j}]: ')))

def Maior_10(Matriz):
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if Matriz[i][j] > 10:
                print(f'O valor {Matriz[i][j]}, em ({i}, {j}) é maior que dez!')

Declara_Matriz(Matriz)
print('\n')
Maior_10(Matriz)

#Número 2)
Matriz = [['erro']*5, ['erro']*5, ['erro']*5, ['erro']*5, ['erro']*5]
print('\nNúmero 2)')

def Diagonal_0(Matriz):
    for i in range(len(Matriz)):
        for j in range(len(Matriz[0])):
            if i == j:
                Matriz[i][j] = 1
            else:
                Matriz[i][j] = 0
    for i in range(len(Matriz)):
        for j in Matriz[i]:
            print(f'[{j: ^5}]', end='')
        print()

Diagonal_0(Matriz)

#Número 3)
print('\nNúmero 3)')
Matriz = [[], [], [], []]

def Maior_Matriz(Matriz):
    maior = 0

    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if j == 0 and i == 0:
                maior = Matriz[i][j]
            elif Matriz[i][j] > maior:
                maior = Matriz[i][j]

    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if Matriz[i][j] == maior:
                print(f'O maior valor da Matriz é {maior}, na/nas coordenada/as [(]{i}, {j}]')

Declara_Matriz(Matriz)
print('\n')
Maior_Matriz(Matriz)

#Número 4)
print('\nNúmero 4)')
Matriz = [[], [], [], [], []]

def Busca_X(Matriz, X):
    booleano = True
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if Matriz[i][j] == X:
                print(f'Encontrei {X} em [{i}, {j}]')
                booleano = False
    if booleano:
        print('Não encontrado')

#Número 5)a)
Matriz = [[], [], []]

def Media_Total(Matriz):
    soma = qnt = 0
    for i in range(len(Matriz)):
        for j in range(len(Matriz)):
            soma += Matriz[i][j]
            qnt += 1
    return soma/qnt
Declara_Matriz(Matriz)
print(f'\nA média dos valores dessa Matriz é {Media_Total(Matriz)}\n')

for i in range(len(Matriz)):
    for j in range(len(Matriz[i])):
        print(f'[{Matriz[i][j]: ^5}]', end='')
    print()
    #Mostrar a Matriz
print('\n')

#b)
def Media_Linha(Matriz):
    soma = 0
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            soma += Matriz[i][j]
        print(f'A média da linha {i} é {soma/len(Matriz[i])}')
        soma = 0

Media_Linha(Matriz)
print('\n')

#c)
def Maior_Elemento(Matriz):
    maior = 0

    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if j == 0 and i == 0:
                maior = Matriz[i][j]
            elif Matriz[i][j] > maior:
                maior = Matriz[i][j]

    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if Matriz[i][j] == maior:
                print(f'O maior valor da Matriz é {maior}, na/nas coordenada/as ({i}, {j})')

Maior_Elemento(Matriz)

#d)
def Maior_Soma_Linha(Matriz):
    soma = maior = posi = 0
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            soma += Matriz[i][j]
        if i == 0:
            maior = soma
            posi = i
        elif Matriz[i][j] < soma:
            maior = soma
            posi = i
    print(f'\nA lista com maior soma é a {posi}, com valor {maior}')

Maior_Soma_Linha(Matriz)

#e)
def Soma_Diagonal(Matriz):
    soma = 0
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if i == j:
                soma += Matriz[i][j]
    return soma

print(f'\nA soma dos elementos da coluna principal é {Soma_Diagonal(Matriz)}\n')

#f)
def Média_Par(Matriz):
    soma = 0
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if i%2 == 0:
                soma += Matriz[i][j]
    return soma

print(f'A Média das Linhas pares é {Média_Par(Matriz)}')

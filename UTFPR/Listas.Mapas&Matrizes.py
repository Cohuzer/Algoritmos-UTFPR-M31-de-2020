from random import randint
#MAPAS
aluno = list()
notas = list()
boletim = dict()
media = 0
print('Mapas: Número 1)')
for i in range(5):
    aluno.append(str(input(f'Nome do {i + 1}° aluno: ')))
    notas.append(float(input(f'Nota de {aluno[i]}: ')))
boletim['Alunos'] = aluno[:]
boletim['Notas'] = notas[:]
print('\nMapas: Número 2)')
for i in boletim['Notas']:
    media += i
print(f'A média das notas de todos os alunos é {media/len(boletim["Alunos"])}')

#MATRIZ
print('\nMATRIZ')
Matriz = [[0]*3, [0]*3, [0]*3]
somaG = somaL = somaC = 0

def randomizar_matriz (Matrix):
    for i in range(3):
        for j in range(3):
            Matrix[i][j] = randint(0, 100)
    for i in range(3):
        for j in Matrix[i]:
            print(f'[{j: ^5}]', end='')
        print()

def somar_toda_matriz (Matrix,soma):
    for i in range(3):
        for j in range(3):
            soma += Matrix[i][j]
    print(f'A soma dos itens da matriz é {soma}')

def somar_colunas_matriz (Matrix, soma):
    for j in range(3):
        for i in range(3):
            soma += Matrix[i][j]
        print(f'A média dos itens da coluna {j} é {soma/len(Matriz[i]):.2f}')
        soma = 0

def somar_linha_matriz (Matrix, soma):
    for i in range(3):
        for j in range(3):
            soma += Matrix[i][j]
        print(f'A média dos itens da linha {i} é {soma/len(Matriz[i]):.2f}')
        soma = 0

print('Matriz:')
randomizar_matriz(Matriz)
print('\n1)', end='')
somar_toda_matriz(Matriz, somaG)
print('\n2)', end='')
somar_linha_matriz(Matriz, somaL)
print('\n3)', end='')
somar_colunas_matriz(Matriz, somaC)

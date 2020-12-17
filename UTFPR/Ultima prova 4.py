Matriz = [[], [], [], [], []]
for i in range(len(Matriz)):
    for j in range(5):
        Matriz[i].append(int(input(f'Digite o número da coordenada ({i}, {j}): ')))

def Mostra_Matriz(Matriz):
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            print(f'[{Matriz[i][j]: ^5}]', end='')
        print()

Mostra_Matriz(Matriz)
print('\n')

for i in range(len(Matriz)):
    anterior = Matriz[i][0]
    booleano = True
    for j in range(len(Matriz[i])):
        if Matriz[i][j] != anterior: 
            booleano = False
        else: 
            anterior = Matriz[i][j]
    if booleano:
        print(f'A linha {i} tem todos os valores iguais')

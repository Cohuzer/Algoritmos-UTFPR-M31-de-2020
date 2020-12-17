from random import randint

Matriz = [
 [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)],
 [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)],
 [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)], 
 [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)],
 [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
  ]
def Mostra_Matriz(Matriz):
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            print(f'[{Matriz[i][j]: ^5}]', end='')
        print()

Mostra_Matriz(Matriz)
y = -1

for i in range(len(Matriz)):
    for j in range(len(Matriz[i])):
        if j == i:
            if Matriz[i][y]%2 != 0:
                print(f'O elemento {Matriz[i][y]}, na linha {i} da diagonal secundaria é impar')
            y -= 1
    
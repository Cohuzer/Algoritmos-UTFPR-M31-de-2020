add = int(0)
qnt = int(0)
entrada = int(1)

while entrada > 0:
    entrada = int(input('Insira um número inteiro positivo [Zero ou negativos para parar]: '))
    if entrada > 0:
        add += entrada
        qnt += 1
        print('Registrado com sucesso')
    else:
        print('Você digitou um número negativo/zero')

print(f'Você digitou {qnt} números válidos, aos quais:\nA sua soma é {add}\nA sua média é {add/qnt:.2f}')

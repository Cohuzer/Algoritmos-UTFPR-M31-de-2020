def comparar (primeiro, segundo):
    if primeiro == segundo:
        return print('São Iguais')
    else:
        return print('São diferentes')

cont = 0
i = 0

entrada = str(input('Insira uma palavra/frase: '))
print(entrada[-1])

entrada2 = str(input('Insira outra string: '))
comparar(entrada, entrada2)

nome = str(input('Insira um nome: ')).capitalize()
nome2 = str(input('Insira outro nome: ')).capitalize()
comparar(nome[0], nome2[0])

entrada3 = str(input('Uma string para ser invertida: '))
print(entrada3[::-1])
entrada4 = str(input('String para contar as vogais: ')).lower()
for i in range(0, len(entrada4)):
    if entrada4[i] in 'aeiouéóúíáâêîôûãeiõuà':
        cont += 1
    i += 1
print(f'Em {entrada4} temos {cont} vogais')

minum = str(input('Input pra minusculo: ')).lower()
max = str(input('Input para maiusculo: ')).upper()
print(minum, max)

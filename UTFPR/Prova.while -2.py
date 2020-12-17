txt = str('S')
desconto = int(0)

while txt == 'S':
    valor = float(input('Insira o valor do carro (sem desconto): '))
    ano = int(input('Insira o ano de fabricação do veículo: '))
    if ano <= 2010:
        desconto = float(valor * 0.2)
    elif ano <= 2020:
        desconto = float(valor * 0.15)
    elif ano > 2020:
        desconto = float(valor * 0.1)
    print(f'Com um desconto de R${desconto:.2f} o carro passa a custar R${valor - desconto:.2f}')
    txt = str(input('Deseja continuar [S/N]? ')).upper()
    while txt != 'S' and txt != 'N':
        txt = str(input('Opção inválida\nDeseja continuar [S/N]? ')).upper()
print('\033[1;31mFIM DO PROGRAMA')
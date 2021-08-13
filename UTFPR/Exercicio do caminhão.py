c_total= float(input('\033[1;33mCAPACIDADE DO CAMINHÃO (Kg): '))
cx = float(input('VALOR DA CAIXA (Kg): '))
qnt_c = int(0)
resto = c_total
acumulo = cx

qnt_c += 1
resto -= cx
if cx == c_total:
    print('Esta caixa tem o peso exato que o caminhão aguenta transportar')
if cx > c_total:
    print(f'Esta caixa é mais pesada que a capacidade do caminhão por {cx - c_total} Kg')
else:
    print(f'Você pode colocar {resto} Kg no caminhão, nele há {acumulo} Kg acumulados, no total {qnt_c} caixa')
while cx <= c_total:
    cx = float(input('VALOR DA CAIXA: '))
    qnt_c += 1
    resto -= cx
    acumulo += cx
    if acumulo > c_total:
        print(f'Você passou do limite do caminhão em {acumulo - c_total} Kg, com {qnt_c} caixas e no total {acumulo} Kg')
        break
    elif acumulo == c_total:
        print(f'Você chegou na capacidade do caminhão com {qnt_c} caixas, tendo um total de {acumulo} Kg')
        break
    else:
        print(f'Você pode colocar {resto} Kg no caminhão, nele tem {qnt_c} caixas')
print('Obrigado')

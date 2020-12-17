qntP = int(0)
somaP = int(0)
qnt3 = int(0)
soma3 = int(0)
qntT = int(0)
somaT = int(0)
i = int(10)
while i != 51:
    if i%2 == 0:
        qntP += 1
        somaP += i
    if i%3 == 0:
        qnt3 += 1
        soma3 += i
    if i%2 == 0 and i%3 == 0:
        qntT += 1
        somaT += i
    i += 1
print(f'No intervalo fechado de 10 a 50 temos:\n{qntP} números pares, os quais tem média {somaP/qntP}\n'
      f'{qnt3} números divisiveis por 3, os quais tem média {soma3/qnt3}\n'
      f'{qntT} números pares e divisiveis por 3, os quais tem média {somaT/qntT}')

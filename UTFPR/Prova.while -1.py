qnt = int(input('Insira a quantidade de pessoas a serem analisadas: '))
i = int(0)
qntM = int(0)
qntF = int(0)

while i != qnt:
    sex = str(input('Insira o sexo da pessoa analisada [M/F]: ')).upper()
    while sex != 'F' and sex != 'M':
        sex = str(input('\033[1;31mOpção inválida!\033[m\n Insira o sexo da pessoa analisada [M/F]: ')).upper()
    if sex == 'M':
        print('Registrado com sucesso!')
        qntM += 1
        i += 1
    if sex == 'F':
        print('Registrada com sucesso!')
        qntF += 1
        i += 1

print(f'De {qnt} pessoas analisadas, {qntM} são do sexo Masculino e {qntF} são do sexo Feminino\n{(qntF * 100)/qnt:.1f}% são mulheres e {(qntM * 100)/qnt:.1f}% são homens')

qF = int(0)
qM = int(0)
qTotal = int(input('Quantas pessoas serão analizadas? '))
i = int(0)
while qTotal != i:
    sexo = str(input('Insira o sexo [M/F]: ')).upper()
    while sexo not in 'FM':
        sexo = str(input('Opção inválida. Insira o sexo [M/F]: ')).upper()
    if sexo == 'M':
        qM = qM + 1
        i = i + 1
    if sexo == 'F':
        qF = qF + 1
        i = i + 1
print(f'De {qTotal} pessoas, {(qF*100)/qTotal:.1f}% são do sexo feminino e {(qM*100)/qTotal:.1f}% são do sexo masculino')

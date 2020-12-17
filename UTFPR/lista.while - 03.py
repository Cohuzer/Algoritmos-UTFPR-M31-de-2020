manuel = float(1.60)
paulo = float(1.20)
ano = int(0)
while paulo < manuel:
    manuel = manuel + 0.02
    paulo = paulo + 0.03
    ano = ano + 1
print(f'Em {ano} anos Paulo será maior que Manuel, Paulo com {paulo:.2f} metros e Manuel com {manuel:.2f}')

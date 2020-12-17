a = int(0)
b = int(0)
c = int(0)
qnt = int(input('Quantas pessoas vão votar?'))
i = int(0)
voto = int(0)
while qnt != i:
  voto = int(input('''Para qual candidato você votara?\nDigite 1 para o candidato 1\nDigite 2 para o candidato 2\nDigite 3 para o candidato 3'''))
  if voto == 1:
    a += 1
    i += 1
  if voto == 2:
    b += 1
    i += 1
  if voto == 3:
    c += 1
    i +=1
  else:
    print('Opção invalida')
print(f'Dos {qnt} votos, o candidato 1 recebeu {a} votos, o candidato 2 recebeu {b} votos e o candidato 3 recebeu {c} votos.')

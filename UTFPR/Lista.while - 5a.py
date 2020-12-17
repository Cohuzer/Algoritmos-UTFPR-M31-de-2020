i = int(10)
total = int(0)
cont = int(0)
while i <= 50:
    if i%5 == 0:
        total = total + i
        cont += 1
    i += 1
print(f'A média dos núemros divisiveis por 5 entre 10 e 50 é {total/cont}')

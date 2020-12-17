A = [22, 4, 55, 300, 25, 1, 45, 2020, 99, 54]
pares = list()
impares = list()
divisiveis_3 = list()
media_3 = 0

for i in A:
    if i%2 == 0:
        pares.append(i)
    if i%2 != 0:
        impares.append(i)
    if i%3 == 0:
        divisiveis_3.append(i)
        media_3 += i

print(f'\033[1;36mNúmeros Pares => {pares}\nNúmeros Impares => {impares}\nNúmeros divisiveis por 3 => {divisiveis_3}')
print(f'A soma dos números divisiveis por 3 é {media_3}\nE a Média dos divisiveis por 3 é {media_3/len(divisiveis_3)}')

i = 0
impar = 0
quantidade_impar = 0
par = 0
divisivel_5 = 0
quantidade_divisivel_5 = 0

print('\033[1;34mNÚMERO #1')
for i in range(10, 51):
    if i%5 == 0:
        divisivel_5 += i
        quantidade_divisivel_5 += 1
    if i%2 != 0:
        impar += i
        quantidade_impar += 1
    if i%2 == 0:
        par += i

print(f'A média de números impares entre 10 e 50 é {impar/quantidade_impar}')
print(f'A média de números divisiveis por 5 entre 10 e 50 é {divisivel_5/quantidade_divisivel_5}')
print(f'A soma dos números pares entre 10 e 50 é {par}')

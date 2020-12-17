m = input(int('Insira o valor em metros cúbicos da água utilizada: '))
while m != 40:
    if m <= 5:
        a = 69.79
    elif m <= 10:
        a = 69.79 + (m-5)*2.16
    elif m <= 15:
        a = 69.79 + 5*2.16 + (m-10)*12.02
    elif m <= 20:
        a = 69.79 + 5*2.16 + 5*12.02 + (m-15)*12.10
    elif m <= 30:
        a = 69.79 + 5*2.16 + 5*12.02 + 5*12.10 + (m-20)*12.19
    else:
        a = 69.79 + 5*2.16 + 5*12.02 + 5*12.10 + 10*12.19 + (m-30)*20.63
    print(f'({m},{a:.2f})')
    m += 1

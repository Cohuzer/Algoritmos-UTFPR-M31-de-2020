def Inverter(palavra):
    palavra = palavra.split()
    for i in palavra:
        print(i[::-1], end=' ')


entrada = str(input('Insira uma frase: '))
Inverter(entrada)

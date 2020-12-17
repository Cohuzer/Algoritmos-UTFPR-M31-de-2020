#Uma pesquisa sobre algumas características físicas da população de uma determinada região coletou os seguintes dados, referentes a cada habitante, para serem analisados:
#- Sexo (Masculino, Feminino)
#- Cor dos olhos (Azul, Verde, Castanho, Preto)
#- Cor dos cabelos (Loiro, Castanho, Preto)
#- Idade
#Fazer um código que determine e escreva:
#a) A maior Idade dos habitantes.
#b) O percentual dos indivíduos do sexo feminino cuja a idade esteja entre 18 e 35 anos (inclusive) e que tenham olhos castanhos e cabelos loiros.
txt = str('S')
maior_idade = int(0)
qnt = int(0)
final= int(0)

while txt in 'Ss':
    sex = str(input('Insira o sexo [M/F]: ')).upper()
    cabelo = str(input('Insira a cor do cabelo [Loiro/Castanho/Preto/Ruivo]:')).capitalize()
    olhos = str(input('Insira a cor dos olhos [Azul/Verde/Preto/Castanho]: ')).capitalize()
    idade = int(input('Insira a idade: '))
    qnt = qnt + 1
    if idade > maior_idade:
        maior_idade = idade
    if sex == 'F' and 18 <= idade <= 35 and olhos == 'Castanho' and cabelo == 'Loiro':
        final += 1
    txt = str(input('Quer continuar [S/N]? '))

print(f'De {qnt} pessoas {final}, ou {(final*100)/qnt:.1f}%, são mulheres com idades entre 18 e 35 anos, que tem olhos castanhos e são loiras')
print(f'Dentre as pessoas analisadas a maior idade é {maior_idade}')

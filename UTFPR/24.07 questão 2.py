#Construa um código que calcule a área total de uma residência (sala, cozinha, quartos, etc., sendo todos eles retangulares). O usuário deverá informar com a largura (L) e o comprimento (C) de cada cômodo da casa. Em seguida deverá ser apresentada uma pergunta, solicitando a confirmação do usuário para continuar com a entrada de dados (a confirmação será dada quando o usuário entrar com “S”). Caso ele entre com o valor “N”, o laço termina e deverá ser apresentada a área total da casa.
#OBS:. Não se esqueça de validar a entrada da resposta do usuário, que só pode aceitar os caracteres “S” ou “N”.
total = int(0)
txt = str('S')
while txt in 'Ss':
    L = float(input('Insira a largura do cômodo (em metros): '))
    C = float(input('Insira o comprimento do cômodo (em metros): '))
    total = total + (L*C)
    txt = str(input('Deseja continuar? [S/N]: '))
    while txt not in 'NnSs':
        txt = str(input('Opção Inválida, insira novamente \nDeseja continuar? [S/N]: '))
print(f'A área total da residência é de {total} metros ao quadrado')

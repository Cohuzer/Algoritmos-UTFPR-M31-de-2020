def cria_cidade(dict, num):
    for i in range(num):
        escopo = str(input('Nome da cidade: '))
        dict['Nome'][i] = escopo
        escopo = int(input(f'Quantos habitantes existem em {escopo}: '))
        dict['Habitantes'][i] = escopo 
    return dict

def media_hab(dict):
    media = 0
    for i in dict['Habitantes']:
        media += i
    media /= len(dict['Habitantes'])
    print(f'\nA média de habitantes das cidades é {media:.2f}\n')
    return media

def abaixo_media(media, dict):
    escopo = []
    for i in range(len(dict['Habitantes'])):
        if dict['Habitantes'][i] < media:
            escopo.append([dict['Nome'][i], dict['Habitantes'][i]])
    return escopo

qnt = int(input('Quantas cidades serão catalogadas? '))
Atlas = {
    'Nome': [0]*qnt,
    'Habitantes': [0]*qnt
}

Atlas = cria_cidade(Atlas, qnt)

media = media_hab(Atlas)
abaixo = abaixo_media(media, Atlas)
for i in range(len(abaixo)):
    print(f'A cidade {abaixo[i][0]} esta abaixo da média, com {abaixo[i][1]} habitantes')

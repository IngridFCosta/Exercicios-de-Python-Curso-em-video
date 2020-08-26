"""073- Crie uma tupla preenchida com os 20 primeiros
colocados da tabela do campeonato brasileiro de futebol,
na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os ultimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabética
d) Em que posição na tabela está o time da Chapecoense
"""
times=('Flamengo','Santos','Palmeiras','Grêmio','Atlético-PR','São Paulo', 'Internacional','Corinthians',
       'Fortaleza','Goiás','Bahia','Vasco','Atlético-MG','Fluminense','Botafogo','Ceará','Cruzeiro','CSA',
       'Chapecoense','Avaí')
#a)
primeiros=times[0:5]
print(f'Os 5 primeiros colocados são: {primeiros}')
#b)
ultimos=times[-4:]
print(f'Os 4 ultimos colocados são: {ultimos}')
#c
ordemAlfa=sorted(times)
print('Ordem alfabética')
print(ordemAlfa)
#d
posChape=times.index('Chapecoense')+1
print(f'A chapecoense está na {posChape}ª posição.')

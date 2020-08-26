"""069- Crie um  programa que leia a idade e o sexo
de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
"""


mais18=0
homem=0
mulherM20=0
while True:
    print('-'*35)
    print('Realize o cadastro')
    print('-' * 35)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo: F/M ')).strip().upper()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? S/N ')).upper().strip()
    if idade > 18:
        mais18+=1
    if sexo =='M':
        homem+=1
    if sexo =='F' and idade < 20:
        mulherM20+=1
    if resposta == 'N':
            break
print('-'*35)
print(f'Pessoas com mais de 18 anos: {mais18}')
print(f'Número de homens cadastrado: {homem}')
print(f'Mulheres com menos de 20 anos: {mulherM20}')
print('-'*35)

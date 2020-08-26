"""094- Crie um programa que leia nome, sexo e idade de
 várias pessoas, guardando os dados de cada pessoa em um
 dicionário e todos os dicionarios em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas com idade acima da média
 """

cadastro={}
listaCadastro=[]
listaMulher=[]
mediaidade=soma=0
while True:
    cadastro.clear()
    cadastro['Nome']=str(input('Escreva o nome: '))
    cadastro['idade']=int(input('Escreva a idade:'))
    soma+=cadastro['idade']
    cadastro['Sexo']=str(input('Escreva o sexo: (M/F) ')).upper().strip()[0]
    listaCadastro.append(cadastro.copy())
    continuar=' '
    continuar=str(input('Deseja continuar? (S/N)')).upper().strip()[0]
    while continuar not in 'SN':
        print('Você digitou um dado inválido!Tente novamente!')
        continuar = str(input('Deseja continuar? (S/N)')).upper().strip()[0]
    if continuar=='N':
        print('Programa encerrado!')
        break
    while cadastro['Sexo'] not in 'MF':
        print('Você digitou um dado inválido!Tente novamente!')
        cadastro['Sexo'] = str(input('Escreva o sexo: (M/F) ')).upper().strip()[0]
print(listaCadastro)

print(f'Total de pessoas cadastradas: {len(listaCadastro)}')
mediaidade=soma/len(listaCadastro)
print(f'A média de idades é de {mediaidade:5.2f} anos')
print('As mulheres cadastradas foram: ', end='')

for p in listaCadastro:
    if p['Sexo']=='F':
        print(f'{p["Nome"]}', end='')
print()
print('As pessoas com idade acima da média são: ', end='')
for idade in listaCadastro:
    if idade['idade'] > mediaidade:
        print(f'{idade["Nome"]}', end='')
        #print('    ', end='')
        #for k, v in idade.items():
        #   print(f'{k} = {v}: ', end='')
        #print()

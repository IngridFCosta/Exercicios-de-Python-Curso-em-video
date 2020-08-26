"""061- Refaça o DESAFIO  051, lendo o primeiro termo e
a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando while"""

#Usando a formula
primeiroTermo=int(input('Escreva o primeiro termo da PA: '))
razao=int(input('Escreva a razão da PA: '))
i=1
while i<=10:
    x=primeiroTermo+(i-1)*razao
    print(x,end='->')
    i=i+1
print('FIM')

#Sem a Formula
primeiroTermo=int(input('Escreva o primeiro termo da PA: '))
razao=int(input('Escreva a razão da PA: '))
termo=primeiroTermo
cont=1
while cont<=10:
    print('{} ->'.format(termo), end='')
    termo+=razao
    cont+=1
print('FIM')


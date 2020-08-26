"""051- Escreva um programa que leia o primeiro termo
e a razão de uma PA. No final mostre os 10 primeiros
termos dessa progressão
"""
#Formula- an=a1+(n-1)*r
pTermo=int(input('Escreva o primeiro termo da PA: '))
razaoPA=int(input('Escreva a razão da PA:'))
print('\033[36m-'*35)
print('Os 10 primeiros termos da PA são:\033[m')
for contagem in range(1,11):
    x=pTermo+(contagem-1)*razaoPA
    print(x,end='-> ')
print('FIM')


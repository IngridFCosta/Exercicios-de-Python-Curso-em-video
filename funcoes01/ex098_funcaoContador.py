"""098- Faça um programa que tenha uma função
chamada contador(), que receba três parametros:
inicio, fim, passo e realize a contagem.
Seu programa tem que realizar três contagens
através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada.
"""
def contador(inicio, fim, passo):
    if passo < 0:
        passo*= -1
    if passo == 0:
        passo= 1
    print(f'Contagem de  {inicio} a {fim} de {passo} em {passo}')

    if inicio < fim:
        cont=inicio
        while cont <=fim:
            print(f'{cont}', end=' ')
            cont+=passo
        print('FIM!')
    else:
        cont=inicio
        while cont >=fim:
            print(f'{cont}', end=' ')
            cont-=passo
        print('FIM!')


contador(1,10,1)
contador(10,0,2)
print('Personalize a contagem!')
i=int(input('Inicio:  '))
f=int(input('Fim:     '))
p=int(input('Passo:   '))
contador(i,f,p)




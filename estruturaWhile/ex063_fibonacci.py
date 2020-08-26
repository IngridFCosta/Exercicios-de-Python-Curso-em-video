"""063- Escreva um programa que leia  um numero n
inteiro qualquer e mostre na tela os n primeiros elementos
de uma sequencia de Fibonacci
ex- 0-1-1-2-3-5-8
"""

"""
1º passo: definir e atribuir os valores as variavéis do primeiro e segundo termos
2º atibuir 3 ao contador -A partir do terceiro
3º 
"""
numTermos= int(input('Quantos termos você quer mostrar? '))
t1=0
t2=1
cont=3
print('{} -> {}'.format(t1,t2), end='')
while cont <=numTermos:
    t3 = t1 + t2 #soma dos dois anteriores
    print('-> {}'.format(t3),end='')
    t1=t2 #mudança de posição
    t2=t3
    cont+=1
print('-> FIm')
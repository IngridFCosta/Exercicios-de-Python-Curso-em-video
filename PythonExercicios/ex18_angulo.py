"""
ex18- Faça um programa que leia um ângulo qualquer e mostre na tela
 o valor do seno, cosseno e tagente desse angulo.

"""
import math
angulo=int(input('Escreva um angulo: '))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print('Angulo: {}°, seno: {:.3f}, cosseno: {:.3f}, tangente: {:.3f}'.format(angulo,seno,cosseno,tangente))

# 010- Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre
# quantos  dólares ela pode comprar.

Valdolar=5.31
real=float(input('Diga quantos reais você tem na carteira:'))
dEmDolar=real/Valdolar
print('Você pode comprar {:.2f} dolares'.format(dEmDolar))


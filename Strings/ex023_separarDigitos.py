"""023- faça um programa que leia um numero
de 0 a 9999 e mostre na tela cada um dos digitos
separados."""

numero=int(input('Escreva um numero inteiro: '))
unidade=numero//1%10
dezena=numero//10%10
centena=numero//100%10
milhar=numero//1000%10

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
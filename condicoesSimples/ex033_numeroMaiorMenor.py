"""Faça um programa que leia três números e mostre qual é o maior e qual o menor"""

primeiro=int(input('Escreva o primeiro número:'))
segundo=int(input('Escreva o segundo número:'))
terceiro=int(input('Escreva o terceiro número:'))
#VERIFICANDO QUEM É MENOR
menor=primeiro
if segundo<primeiro and segundo<terceiro:
    menor=segundo
if terceiro < primeiro and terceiro>segundo:
    menor=terceiro

maior=primeiro
if segundo> primeiro and segundo>terceiro:
    maior=segundo
if terceiro > primeiro and terceiro >segundo:
    maior=terceiro
print('O maior valor digitado foi:{} '.format(maior))
print('O menor valor digitado foi:{} '.format(menor))
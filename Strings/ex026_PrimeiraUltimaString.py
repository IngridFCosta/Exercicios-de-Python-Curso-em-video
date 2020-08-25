"""026- Faça um programa que leia uma frase
pelo teclado e mostre:
-quantas vezes aparecea letra 'A'
-em que posição ela aparece a
primeira vez
-em que posição ela aparece
a ultima vez."""

frase=str(input('Escreva uma frase: ')).upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A aparece a ultima vez na posição {}'.format(frase.rfind('A')+1))
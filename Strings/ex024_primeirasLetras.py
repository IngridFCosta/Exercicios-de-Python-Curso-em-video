"""024-Crie um programa que leia o nome
de uma cidade e diga se ela começa ou não
 com o nome 'SANTO' """

cidade=str(input('Escreva o nome da sua cidade de nascimento:'))
print(cidade[:5].upper()=='SANTO')
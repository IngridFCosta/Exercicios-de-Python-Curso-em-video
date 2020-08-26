"""065- Crie um programa que leia vários números
inteiros pelo teclado. No final da execucção,
mostre a média entre todos os valores e qual foi
o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer ou não continuar
a digitar valor."""

soma=0
qtd=0
continuar='S'
maior= menor=0
while continuar=='S':
    valor=int(input('Escreva um valor:'))
    continuar=str(input('Deseja continuar? ')).upper()
    soma=soma+valor
    qtd+=1
    if qtd ==1:
        maior=menor=valor
    else:
        if valor> maior:
            maior=valor
        if valor < menor:
            menor=valor

print(f'A media é igual a:{soma/qtd}')
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')




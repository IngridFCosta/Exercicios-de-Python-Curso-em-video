"""050- Desenvolva um programa que leia seis números
inteiros  e mostre a soma apenas daqueles que foram
pares.Se o valor digitado foi impar, desconsidere-o.
"""

soma=0
for contador in range(1,7):
    numero=int(input('Escreva um valor: '))
    if numero%2==0:
        soma=soma+numero
print('A soma dos valores pares é igual a:{} '.format(soma))
"""
013- Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
"""
salario= float(input('Escreva o salário:'))
novoSalario=salario+(salario*15/100)
print('O novo salário é igual a: {}'.format(novoSalario))
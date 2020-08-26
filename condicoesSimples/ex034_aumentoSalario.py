"""034-Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.
Para Salários superiores a R$1200,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
salario=float(input('Escreva o valor do salário'))
if salario > 1200.00:
    aumento= (salario *10)/100
    novoSalario=salario+aumento
    print('\033[7;44mO valor do aumento foi de {:.2f}'.format(aumento))
    print('O funcionário passará a receber {:.2f}'.format(novoSalario))
else:
    aumento = (salario * 15) / 100
    novoSalario = salario + aumento
    print('\033[7;44mO valor do aumento foi de {:.2f}'.format(aumento))
    print('O funcionário passará a receber {:.2f}'.format(novoSalario))

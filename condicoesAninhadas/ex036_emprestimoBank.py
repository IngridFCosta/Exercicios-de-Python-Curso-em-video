""""036- Escreva um programa para aprovar o emprestimo bancario
para a compra de uma casa. O programa vai perguntar o valor da casa,
o sálario do comprador e em quantos anos ele vai pagar.
-Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
"""
valorCasa= float(input('Qual o valor da casa?'))
salarioComprador= float(input('Qual o salario do comprador?'))
anosPag=int(input('Em quantos anos deseja pagar?'))

prestacao=valorCasa/(anosPag*12)
percentualSal=(salarioComprador*30)/100

print('O valor da prestação é:{}'.format(prestacao))
if prestacao > percentualSal:
    print('Emprestimo negado! A prestação excede 30% do seu salario.')
elif prestacao <= percentualSal:
    print('Emprestimo aceito!')


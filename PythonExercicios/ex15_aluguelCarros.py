"""exe15- Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa
60 reais por dia e 0.15 por km rodado.
"""
qtdKM=float(input('Escreva a quantidade de km percorridos: '))
dias=int(input('Escreva a quantidade de dias: '))
preco= (dias*60)+(qtdKM*0.15)
print('O preço a pagar será igua a: {:.2f} R$'.format(preco))
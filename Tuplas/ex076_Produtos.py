"""076- Crie um programa que tenha uma tupla única
com nomes de produtos e seu respectivos  preços na
sequencia.

No final, mostre uma listagem de preços, organizando
oos dados de forma tabular
"""
print('='*40)
print(f'{"Tabela de Preços":^40}')
print('='*40)
produtos=('Arroz', 2.50, 'Feijao', 3.50, 'Açucar', 2.20, 'Café', 2.60, 'Detergente', 2.85 )

for cont in range(0,len(produtos)):
   if cont%2==0:
       print(f'{produtos[cont]:.<30}', end='')
   else:
       print(f'R${produtos[cont]:>7.2f}')



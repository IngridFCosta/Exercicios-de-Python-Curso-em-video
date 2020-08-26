import ex109.moeda

preco=float(input('Escreva o valor R$: '))
aumento=float(input('Escreva o aumento (%):'))
decrescimo=float(input('Escreva o valor do decrescimo: '))


valorAumento= ex109.moeda.aumentar(preco, aumento,True)
print(f'O valor com o aumento de {aumento} % é {valorAumento}')

valorDecrescimo= ex109.moeda.diminuir(preco, decrescimo, True)
print(f'O Valor com o desconto de {decrescimo}% é {valorDecrescimo}')

valorDobro= ex109.moeda.dobro(preco,True)
print(f'O dobro de {preco} é {valorDobro}')


valormetade= ex109.moeda.metade(preco,True )
print(f'A metade de {preco} é {valormetade}')





import ex107.moeda

preco=float(input('Escreva o valor R$: ')).ex
aumento=float(input('Escreva o aumento (%):'))
decrescimo=float(input('Escreva o valor do decrescimo: '))


valorAumento= ex107.moeda.aumentar(preco, aumento)
print(f'O valor com o aumento de {aumento} % é {valorAumento}')

valorDecrescimo= ex107.moeda.diminuir(preco, decrescimo)
print(f'O Valor com o desconto de {decrescimo} é {valorDecrescimo}')

valorDobro= ex107.moeda.dobro(preco)
print(f'O dobro de {preco} é {valorDobro}')


valormetade= ex107.moeda.metade(preco)
print(f'A metade de {preco} é {valormetade}')





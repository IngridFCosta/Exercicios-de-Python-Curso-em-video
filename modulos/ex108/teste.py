import ex108.moeda

preco=float(input('Escreva o valor R$: '))
aumento=float(input('Escreva o aumento (%):'))
decrescimo=float(input('Escreva o valor do decrescimo: '))


valorAumento= ex108.moeda.aumentar(preco, aumento)
print(f'O valor com o aumento de {aumento} % é {ex108.moeda.moeda(valorAumento)}')

valorDecrescimo= ex108.moeda.diminuir(preco, decrescimo)
print(f'O Valor com o desconto de {decrescimo}% é {ex108.moeda.moeda(valorDecrescimo)}')

valorDobro= ex108.moeda.dobro(preco)
print(f'O dobro de {ex108.moeda.moeda(preco)} é {ex108.moeda.moeda(valorDobro)}')


valormetade= ex108.moeda.metade(preco)
print(f'A metade de {ex108.moeda.moeda(preco)} é {ex108.moeda.moeda(valormetade)}')





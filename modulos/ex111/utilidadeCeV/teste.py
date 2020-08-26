from ex111.utilidadeCeV import moeda
from ex111.utilidadeCeV import dado

preco=dado.leiaDinheiro('Escreva o valor R$: ')
aumento=float(input('Escreva o aumento (%):'))
decrescimo=float(input('Escreva o valor do decrescimo: '))


resumir=moeda.resumo(preco,aumento,decrescimo)



"""044- Elaborar um programa que calcule o valor a ser pago por um
produto, considerando o seu preço normal e condição de pagamento:
-À vista dinheiro /cheque: 10% de desconto:
- À vista no cartão: 5% de desconto
- Em até  2x no cartão: preço normal
- 3x ou mais no cartão: 20% juros
"""

print('\033[0;33m -'*20)
print('1-À vista dinheiro /cheque: 10% de desconto\n'
      '2-À vista no cartão: 5% de desconto\n'
      '3-Em até  2x no cartão: preço normal\n'
      '4- 3x ou mais no cartão: 20% juros\033[m')
print('\033[0;33m -'*20)

condicaoPag= int(input('Informe a condição de pagamento: '))
precoNormal=float(input('informe o preço do produto: '))


#Condições de ppagamento
avDinheiroCheque=1
avCartao=2
cartao_2X= 3
cartao_3X=4

if condicaoPag ==1:
    desconto=(precoNormal*10)/100
    novoPreco=precoNormal-desconto
    print('Você escolheu a opção pagar à vista em  dinheiro /cheque')
    print('Total de desconto R$ {:.2f}. Você pagará {:.2f} reais'.format(desconto,novoPreco))
elif condicaoPag == 2:
    desconto = (precoNormal * 5) / 100
    novoPreco = precoNormal - desconto
    print('Você escolheu a opção pagar à vista no cartão.')
    print('Total de desconto R$ {:.2f}. Você pagará {:.2f} reais'.format(desconto, novoPreco))
elif condicaoPag ==3:
    print('Você escolheu a opção pagar em até  2x no cartão. Nessa opção nao terá desconto')
    print('Você pagará {:.2f} reais'.format())
elif condicaoPag==4:
    print('Você escolheu a opção pagar à vista no cartão.')
    juros=(precoNormal*20)/100
    novoPreco=precoNormal+juros
    print('Você terá que pagar um acrescimo de R$ {:.2f} reais. Seu produto custa {} '.format(juros,novoPreco))
else:
    print('Você cancelou a compra!')
"""066- Crie um programa que leia varios numeros inteiros
pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos
 números foram digitados e qual foi a soma entre elas
 (desconsiderando o FLAG(bandeira))"""

numero=0
soma=0
qtd=0
while numero!= 999:
    numero=int(input('Escreva um numero:'))
    if numero==999:
        break
    else:
        soma=soma+numero
        qtd+=1
print(f'A soma do(s) {qtd} numero(s) é {soma}')


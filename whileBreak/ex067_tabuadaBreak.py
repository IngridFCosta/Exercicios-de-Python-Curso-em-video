"""067- Faça um programa  que mostra a tabuada
de vários numeros, um de cada vez, para cada valor
 digitado pelo usuário. O programa será interrompido
 quando o número solicitado for negativo."""

contador=1
while True:
    numero = int(input('Digite um numero para ver sua tabuada: '))
    if numero < 0:
        print('Programa acabou!')
        break
    limiteTab=int(input('Escreva o limite da sua tabuada:'))
    for contador in range(1, limiteTab + 1):
        print(f'{numero} x {contador} = {numero*contador}')
        contador+=1


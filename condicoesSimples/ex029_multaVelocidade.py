"""029- Escreva um programa que leia a velocidade de um carro.
se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar RS$7,00 por cada km acima do limite.
"""
multa=7.0
velocidade=float(input('Escreva a velocidade do automóvel para calcular o valor da multa:'))

if velocidade > 80.00:
    limite=velocidade-80.00
    valMulta=limite*multa
    print('Você foi multado! Sua multa é de {:.2f}'.format(valMulta))
else:
    print('Parabéns você não excedeu a velocidade')
"""
ex14- Crie um programa que receba uma temperatura em celsius e transforme-a em graus Kelvin e Fahrenheit
"""

celsius=float(input('Escreva uma temperatura em graus celsius:'))
tempFahrenheit=(9*celsius+160)/5
tempKelvin=celsius+273
print('Temperatura em Fahrenheit: {}°'.format(tempFahrenheit))
print('Temperatura em graus Kelvin: {}°'.format(tempKelvin))
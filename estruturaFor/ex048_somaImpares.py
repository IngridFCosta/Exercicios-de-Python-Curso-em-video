"""049- Faça um programa que calcule a soma entre todos os números
impares que são multiplos de três e que se encontrem no intervalo
de 1 até 500.
"""
soma=0
contador=0
for numero in range(1,501):
    if numero%2!=0 and numero%3==0:
        soma=soma+numero
        contador=contador+1
print('\033[0;34mA soma de todos os {} numeros impares divisíveis por três no intervalo de 1 a 500'
      ' é: \033[m\033[0;31m{}\033[m '.format(contador, soma))

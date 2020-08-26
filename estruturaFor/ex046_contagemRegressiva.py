"""046- Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo
entre eles"""

import time
print('Preparando contagemm regressiva')
for contagem in range (10,0,-1):
    print(contagem)
    time.sleep(1)
print('BOOOOOOOOOOOOOOMM!')

"""042-Refaça o desafio numero 035 dos triangulos, acrescentando
o recurso de mostrar que tipo de triangulo será formado:
- Equilatero: Todos os lados iguais
- Isosceles- dois lados iguais
- Escaleno: todos os lados diferentes
"""

ladoA=int(input('Escreva o primeiro lado: '))
ladoB=int(input('Escreva a segundo lado: '))
ladoC=int(input('Escreva o terceiro lado: '))

# soma dos lados
somaAB=ladoA+ladoB
somaAC=ladoA +ladoC
somaBC=ladoB+ladoC

# Verificar se atende as condições para forma um triangulo
if somaAB > ladoC or somaAC >ladoB or somaBC >ladoA:
    print('\033[0;36mForma um triangulo\033[m')
#Testar classificação dos triangulos
    if ladoA == ladoB and ladoA==ladoC:
        print('\033[0;31mO triangulo é equilatero\033[m')
    elif ladoA == ladoB and ladoA!=ladoC:
        print('\033[0;32mO triangulo é isosceles\033[m')
    elif ladoA!=ladoB and ladoA!=ladoC:
        print('\033[0;33mO triangulo é escaleno\033[m')
else:
    print('\033[0;36mNão forma um triangulo!\033[m')


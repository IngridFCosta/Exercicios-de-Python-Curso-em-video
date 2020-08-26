""""096- Faça um programa que tenha uma funçõa
chamada Área(), que receba as dimensões de um terreno
retangular (largura e comprimeento) e mostre a área
do terreno."""
def Area(larg,comp):
    area=largura*comprimento
    print(f'A Area é igual a: {area:.2f} metro(s) ')


largura=float(input('Escreva  a largura: '))
comprimento=float(input('Escreva o comprimento: '))
Area(largura, comprimento)
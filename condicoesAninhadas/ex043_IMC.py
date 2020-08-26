"""043- Desenvolva uma lógica que leia o peso e a altura
de uma pessoa. Calcule seu IMC e mostre seu status, de acordo
com a tabuada abaixo:
- Abaixo de  18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
import math
peso=float(input('Escreva seu peso: '))
altura=float(input('EScreva sua altura: '))
imc=peso/pow(altura,2)
if imc < 18.5:
    print('Seu IMC foi {:.2f}. Você está abaixo do peso!'.format(imc))
elif imc >=18.5 and imc <=25:
    print('Seu IMC foi {:.2f}. Você está no peso ideal!'.format(imc))
elif imc > 25 and imc <=30:
    print('Seu IMC foi {:.2f}. Atenção! Você está com sobrepeso!'.format(imc))
elif imc > 30 and imc <=40:
    print('Seu IMC foi {:.2f}. Cuidado! Você está com obesidade!'.format(imc))
else:
    print('Seu IMC foi {:.2f}. Você está com obesidade mórbida! Procure um médico'.format(imc))


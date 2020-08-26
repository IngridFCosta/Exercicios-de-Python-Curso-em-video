"""
ex17- Escreva um programa que leia o comprimento de um cateto oposto e do cateto adjacente
de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa.
"""
#a²=b²+c²

catetoOp=float(input('Escreva o valor do cateto oposto: '))
catetoAdj=float(input('Escreva o valor do cateto adjacente: '))
hipotenusa=(catetoOp**2)+(catetoAdj**2)
print('A hipotenusa vale:{}'.format(hipotenusa))
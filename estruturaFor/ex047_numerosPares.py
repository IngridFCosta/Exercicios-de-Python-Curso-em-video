"""047- Crie um programa que mostre na tela todos os números
 pares que estão no intervalo entre 1 a 50"""

print('\033[0;;31mOs numeros pares são: \033[m')
for numero in range(1,51):
   if numero%2==0:
     par=numero
     print(par)
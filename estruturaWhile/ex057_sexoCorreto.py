"""057- Faça um programa que leia o sexo de uma pessoa, mas só
aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto
"""
sexo=""
sexo=str(input('Informe  o sexo (M/F): ')).upper().strip()
while sexo !='F' and sexo!= 'M':
    print('Você não informou um sexo válido. Digite novamente')
    sexo=str(input('Informe  o sexo(M/F): ')).upper().strip()
if sexo== 'F' or sexo== 'M':
        print(f'Sexo {sexo} registrado com sucesso!')

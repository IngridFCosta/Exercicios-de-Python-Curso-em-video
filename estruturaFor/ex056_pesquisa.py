"""056- Desenvolva um programa leia o nome,idaade
 e sexo de 4 pessoas. No final do programa mostre:
 - A média da idades do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos.
 """
soma=0
media=0
contagem=0
mVelho=0
for contador in range(1,5):
    print('-----{}ª PESSOA-------'.format(contador))
    nome=str(input('Escreva o nome: '))
    idade=int(input('Escreva a idade: '))
    sexo=str(input('Escreva o sexo: ')).upper()
    soma+=idade
    media=soma/4
if sexo == 'FEMININO' and idade < 20:
    contagem=contagem+1

elif sexo=='MASCULINO':
    if idade > mVelho:
        mVelho=idade
        name=nome
else:
    print('Não tem macho aqui')

print(' A media de idade do grupo é {}:'.format(media))
print('A quantidade de mulheres com menos de 20 anos é: {}'.format(contagem))
print('O nome do homem mais velho é: {}'.format(name))




"""062- Melhore o DESAFIO 061, perguntadno para o usuário
se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser  que quer mostrar 0 termos"""

primeiroTermo=int(input('Escreva o primeiro termo da PA: '))
razao=int(input('Escreva a razão da PA: '))

i=1
while i<=10:
    x=primeiroTermo+(i-1)*razao
    print(x,end='-> ')
    i=i+1
print('\n')

maisTermo=str(input('Deseja mostrar mais termos? S/N:')).upper()
if maisTermo=='S':
        qtdTermo=int(input('Quantos? '))
        i = 1
        while i <= 10+qtdTermo:
            x = primeiroTermo + (i - 1) * razao
            print(x, end='-> ')
            i = i + 1
        print('\n')
        maisTermo=str(input('Deseja mostrar mais termos? S/N:')).upper()

elif maisTermo!= 'S' and maisTermo!= 'N':
    print('Você nao digitou algo válido. Tente novamente!')
    maisTermo = str(input('Deseja mostrar mais termos? S/N:')).upper()
    if maisTermo == 'S':
        qtdTermo = int(input('Quantos? '))
        i = 1
        while i <= 10 + qtdTermo:
            x = primeiroTermo + (i - 1) * razao
            print(x, end='-> ')
            i = i + 1
        print('\n')
        maisTermo = str(input('Deseja mostrar mais termos? S/N:')).upper()
elif maisTermo=='N':
    print('Programa encerrado!')



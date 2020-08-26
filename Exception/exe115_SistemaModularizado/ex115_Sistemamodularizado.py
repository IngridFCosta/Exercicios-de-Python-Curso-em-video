"""115- Crie um pequeno sistema modularizado
que permita cadastrar pessoas pelo seu nome e idade
em um arquivo de texto simples
O sistema só vai ter 2 opções: cadastrar uma nova pessoa
e listar todas as pessoas cadastradas
"""
from exe115_SistemaModularizado.lib.interface import *
from exe115_SistemaModularizado.lib.arquivo import *

arq='Cadastro.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta=menu(['Listar pessoas cadastradas','Cadastrar pessoas', 'Sair do sistema' ])
    if resposta==1:
        lerArquivo(arq)
    elif resposta==2:
       cabeçalho('Nova pessoa')
       nome=str(input('Nome: '))
       idade=leiaint('Idade: ')
       cadastrarPessoa(arq,nome,idade)
    elif resposta==3:
        print('Saindo do sistema')
        break
    else:
        print('Erro!!')
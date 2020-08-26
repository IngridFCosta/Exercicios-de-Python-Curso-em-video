"""114- Crie um código em python que teste se o site
pudim está acessivel pelo computador usado
"""
import urllib
import urllib.request

try:
    site=urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessivel!')
else:
    print('O site está acessivel!')
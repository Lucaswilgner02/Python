import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://instagram.com')
except:
    print('O Site não está acessivel no momento')
else:
    print('Conectado com sucesso!')

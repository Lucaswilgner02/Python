from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas ', 'cadastrar pessoas','Sair do programa '])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo Cadastro ')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3 :
        cabeçalho('\033[33mSaindo do sistema...\033[m')
        break
    else:
        print('\033[31mErro!,Digite uma opção valida.\033[m')
    sleep(2)


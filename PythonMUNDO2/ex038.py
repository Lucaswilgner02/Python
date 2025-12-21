n1=int(input('Digite o Primeiro Número:'))
n2=int(input('Digite o Segundo Número:'))
if n1>n2:
    print('O \033[0:32mPRIMEIRO\033[m NUMERO É MAIOR !')
elif n1<n2:
    print('O \033[0;32mSEGUNDO\033[m NUMERO É MAIOR !')
elif n1 == n2:
    print('\033[0;33mOS NUMEROS SÃO IGUAIS !')

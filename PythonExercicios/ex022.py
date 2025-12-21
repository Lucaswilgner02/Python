n=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusuculas é: {}'.format(n.upper()))
print('Seu nome em minusculas é: {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
#print('seu primeiro nome tem {} letras'.format(n.find(' ')))
separa= n.split()
print('Seu primeiro é {} e tem {} letras'.format(separa[0], len(separa[0])))




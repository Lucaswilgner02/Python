nome=str(input('Qual é o seu nome:'))
if nome=='Lucas':
    print('Que nome bonito!')
elif nome=='Pedro' or nome=='João' or nome=='Maria':
    print('Belo nome')
elif nome=='Gabriel' or nome=='Paulo' or nome=='Sandra':
    print('Você tem um nome legal.')
else:
    print('Seu nome é comum')
print('Tenha um bom dia, {}!!'.format(nome))
sexo = str(input('Qual seu sexo? [M/F]:')).strip().upper()[0]
while sexo not in 'mMfF':
    sexo = str(input('Dados invalidos digite seu sexo novamente: M/F')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

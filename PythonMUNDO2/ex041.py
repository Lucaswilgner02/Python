from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação MIRIM')
elif idade >= 9 and idade < 14:
    print('Classificação INFANTIL')
elif idade >= 14 and idade < 20:
    print('Classificação JUNIOR')
elif idade >= 20 and idade < 26:
    print('classificação SENIOR')
else:
    print('classificação MASTER')


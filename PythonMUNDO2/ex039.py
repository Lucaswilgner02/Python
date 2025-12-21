from datetime import date
atual=date.today().year
ano=int(input('Digite o ano do seu nascimento: '))
idade= atual -ano
print('Quem nascu no ano: {} tem {} anos em {}.'.format(atual,idade,atual))
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    print('Ainda falta {} anos'.format(18-idade))
    saldo = 18-idade
    tempo = atual + saldo
    print('Seu alistamento será: {}'.format(tempo))
elif idade > 18:
    print('Você ja deveria ter se alistado a {} anos'.format(idade-18))
    saldo = idade - 18
    tempo = atual - saldo
    print('O seu alistamento foi em {}.'.format(tempo))


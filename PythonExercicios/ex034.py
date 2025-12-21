salario=float(input('Qual é o seu salario: '))
if salario<=1250:
    novo=salario+(salario*15/100)
else:
    novo=salario+(salario*10/100)
print('quem ganhava R$:{} passa a ganhar R$:{}'.format(salario,novo))

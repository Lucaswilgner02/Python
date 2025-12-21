v=float(input('Qual a sua velocidade? '))
if v>80:
    print('MULTADO! Você excedeu o limite permitido!')
    multa=(v-80)*7
    print('você deve pagar uma multa de R$:{}'.format(multa))
print('Tenha um bom dia!, dirija com segurança')
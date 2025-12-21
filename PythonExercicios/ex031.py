d=float(input('Qual é a distancia da viagem? '))
print('você esta prestes a começar uma viagem de: {}KM'.format(d))
if d<=200:
    p=d*0.50
else:
    p=d*0.45
print('E o preço da sua passagem será de R${:.2f}'.format(p))
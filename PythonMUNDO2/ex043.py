p=float(input('Qual é o seu peso? (Kg):'))
a=float(input('Qual é a sua altura? (m):'))
imc = p / (a**2)
print('O seu imc é: {:.2f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidade!')
else:
    print('Obesidade morbida!')


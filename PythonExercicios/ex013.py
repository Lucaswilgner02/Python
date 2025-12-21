s=float(input('Qual é o salario do funcionario?R$'))
v=s+(s*15/100)
print('um funcionario que ganhava R${:.2f},com 15% de aumento passa a receber R${:.2f}'.format(s,v))
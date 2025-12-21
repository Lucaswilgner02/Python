import random
p=str(input('primeiro aluno:'))
s=str(input('segundo aluno:'))
t=str(input('terceiro aluno:'))
q=str(input('quarto aluno:'))
lista=[p,s,t,q]
escolhido=random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))
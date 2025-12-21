import random
p=str(input('primeiro aluno:'))
s=str(input('segundo aluno:'))
t=str(input('terceiro aluno:'))
q=str(input('quarto aluno:'))
lista=[p,s,t,q]
random.shuffle(lista)
print('a ordem de apresentação será {}'.format(lista))
from random import randint
from time import sleep
comp=randint(0,5)# faz o computador pensar
print('-=-'*20)
print('vou pensar em um numero entre 0 e 5. tente adivinhar qual foi')
print('-=-'*20)
player=int(input('em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if player==comp:
    print('Parabens! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e não no numero {} '.format(player,comp))


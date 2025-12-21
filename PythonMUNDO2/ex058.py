from random import randint
cpu = randint(1, 10)
print('''Sou seu computador...
Acabei de pensar em um número de 1 a 10.
Será que você consegue advinhar?''')
acertou = False
tentativa = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? : '))
    tentativa += 1
    if jogador == cpu:
     acertou = True
    else:
        if jogador < cpu:
            print('Mais... Tente novamente')
        elif jogador > cpu:
            print('Menos... Tente novamente')
print('Parabens voce acertou em {} tentativas'.format(tentativa))
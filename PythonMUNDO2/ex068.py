from random import randint
v = 0
while True:
    print('Vamos jogar Par ou Impar?')
    play = int(input('Digite um numero:'))
    cpu = randint(1,10)
    total = play + cpu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {play} e o computador jogou {cpu} e a soma foi de {total}')
    print(('Deu par ' if total % 2 == 0 else 'Deu impar '))
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu!')
            break
    print('Vamos jogar novamente')
print(f'Game over! você venceu {v} vezes')


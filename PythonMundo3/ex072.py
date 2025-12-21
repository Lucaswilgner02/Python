cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Bloco de entrada inicial (sem loop de repetição)
while True:
    try:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    except ValueError:
        print('Entrada inválida. Tente novamente. ', end='')

print(f'Você digitou o número {cont[num]}.')

# Bloco de continuação (loop principal do programa)
while True:
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] : ')).strip().upper()[0]

    if resp == 'N':
        print('Programa encerrado.')
        break # Sai do loop WHILE principal (que controla a repetição)

    # Se resp == 'S', pede um novo número
    while True:
        try:
            num = int(input('Digite um número entre 0 e 20: '))
            if 0 <= num <= 20:
                print(f'Você digitou o número {cont[num]}.')
                break # Sai deste loop WHILE interno (de validação do número)
            print('Tente novamente. ', end='')
        except ValueError:
            print('Entrada inválida. Tente novamente. ', end='')



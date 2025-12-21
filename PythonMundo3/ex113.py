def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro!,digite um numero inteiro Valido:\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário Preferiu não digitar esse numero\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[;31mErro!,digite um numero Real Valido:\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse numero\033[m')
            return 0
        else:
            return n


num = leiaInt('Digite um numero inteiro: ')
real = leiaFloat('Digite um numero real: ')
print(f'\033[;032mO numero inteiro digitado foi: {num} e o real foi: {real}')
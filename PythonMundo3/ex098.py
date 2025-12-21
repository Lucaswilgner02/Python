from time import sleep
def lin():
    print('-=' * 20)
def contador(i, f, p):
    if p < 0:
       p *= -1
    if p == 0:
       p = 1
    lin()
    print(f'Contagem de {i} até {f} de {p} em {p}:')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont += p
        print('fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont -= p
        print('fim')


contador(1, 10, 1)
contador(10, 0, 1)
lin()
print('Agora é sua vez de personalizar a contagem! ')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
lin()
print('Goodbye!')








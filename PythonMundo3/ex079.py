numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('valor duplicado não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')
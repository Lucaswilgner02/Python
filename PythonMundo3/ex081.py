numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    numeros.count(5)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'voce digitou {len(numeros)} elementos ')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente {numeros}')
if 5 in numeros:
    print('o valor 5 faz parte da lista...')
else:
    print('o valor 5 não faz parte da lista...')

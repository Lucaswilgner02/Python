num = (int(input('Digite um numero: ')),int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),int(input('Digite um numero: ')))
print(f'Os valores digitados foram: {num}')
print(f'O Numero 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O numero 3 está na posição {num.index(3)+1}.')
else:
    print('O numero 3 não foi digitado.')
print(f'Os valores pares digitados foram: {num}')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')



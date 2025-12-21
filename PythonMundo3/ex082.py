num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for i, n in enumerate(num):
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print('-='*30)
print(f'os valores digitados em foram {num}')
print(f'Os valores pares digitados foram {par}')
print(f'Os valores impares digitados foram {impar}')
print('-='*30)


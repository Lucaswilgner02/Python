print('-*'*20)
print('Lojas Super Baratão')
print('-*'*20)
soma = vl1 = menor = cont = 0
pb = ' '
while True:
    cont += 1
    produto = str(input('digite o nome do produto: '))
    valor = float(input('digite o valor do produto: '))
    soma += valor
    if valor >= 1000:
        vl1 += 1
    if cont == 1 or valor < menor:
        menor = valor
        pb = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('deseja continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o valor gasto nas compras {soma}')
print(f'{vl1} produtos custam mais de R$ 1000.00')
print(f'o produto mais barato foi o {pb} e o menor valor pago foi o {menor}')




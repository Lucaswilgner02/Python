listagem = ('lapis','1.75',
            'caneta','2',
            'estojo','3',
            'caderno','15.90',
            'mochila','122.2',
            'marcapasso','23',
            'corretivo','0.80',
            'livro','34.90',
            'borracha', '3.50')
print('-='*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-='*20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        preço_float: float = float(listagem[pos])
        print(f"R${preço_float:>7.2f}")
        print('-='*20)

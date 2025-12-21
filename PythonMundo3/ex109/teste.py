import moeda

p = float(input('Digite o preço: R$ '))


print('-' * 30)
print('SEM FORMATAÇÃO:')
print(f'A metade de {p} é {moeda.metade(p, formatar=False)}')
print(f'O dobro de {p} é {moeda.dobro(p, formatar=False)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, formatar=False)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, formatar=False)}')
print('-' * 30)


print('COM FORMATAÇÃO DE MOEDA:')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, formatar=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, formatar=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, formatar=True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, formatar=True)}')
print('-' * 30)
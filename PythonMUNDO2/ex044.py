print('{:=^40}'.format(' LOJAS WILGNERS '))
preço = float(input('Preço das Compras R$:'))
print('''FORMA DE PAGAMENTO
[ 1 ] á vista no dinheiro/cheque
[ 2 ] á vista no cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opção = int(input('Qual a opção de pagamento? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total= preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total/2
    print('sua compra será parcelada em 2x de R${:.2f} SEM JUROS!'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcela = int(input('Quantas parcelas? '))
    parcela = total/totalparcela
    print('sua compra será parcelada me {}x de R${:.2f} COM JUROS'.format(totalparcela, parcela))
else:
    total = preço
    print('\033[031mOPÇÃO INVALIDA!\033[m')
print('sua compra de R$: {:.2f} vai custar R$ {:.2f}'.format(preço, total))


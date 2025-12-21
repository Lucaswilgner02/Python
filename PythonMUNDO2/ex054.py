from datetime import date
atual=date.today().year
tot=0
tot2=0
for c in range(1, 8):
    p=int(input('Em que ano a {}ª pessoa nasceu?:'.format(c)))
    idade = atual - p
    if idade >= 21:
        tot += 1
    else:
        tot2 += 1
print('temos um total de {} pessoas maiores'.format(tot))
print('temos um total de {} pessoas menores'.format(tot2))


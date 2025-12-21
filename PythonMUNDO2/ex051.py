num=int(input('Primeiro termo: '))
razão=int(input('Razão:'))
décimo= num + (10 - 1) * razão
for c in range (num,décimo + razão,razão):
    print( '{}'.format(c),end= '-> ')
print(' PARA')
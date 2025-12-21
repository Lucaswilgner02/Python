f=str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
#i = ''
i=j[::-1]
#for letra in range(len(j)-1, -1, -1):
  #  i += j[letra] pode ser feito das duas maneiras (remover #)
print('O inverso de {} é {}'.format(j, i))
if i == j:
    print('Temos um PALINDROMO')
else:
    print('NÃO temos um PALINDROMO')


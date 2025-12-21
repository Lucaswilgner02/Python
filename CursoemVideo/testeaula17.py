num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.pop(2)
num.insert(2, 2)
num.insert(3, 10)
print(num)
valores = []
valores.append(2)
valores.append(5)
valores.append(4)
valores.append(6)
valores.append(8)
valores.append(10)
for v in valores:
    print(f'{v}...') # se quiser na mesma linha (,end = '')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c,v in enumerate(valores):
    print(f'\nna posição {c} encontrei o valor {v}...!')
print('cheguei ao final da Lista')

while True:
    n = int(input('digite o numero que deseja saber a tabuada:'))
    print('-'*30)
    if n == 999: break
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('programa finalizado com sucesso')



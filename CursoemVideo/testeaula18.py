'''teste = list ()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''
galera = list()
dado = list()
totma = totmn = 0
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmn += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totma += 1
print(f'Temos {totma} maior e {totmn} menor de idade.')


primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite a Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    cont += 1
    termo += razao
print('Fim')
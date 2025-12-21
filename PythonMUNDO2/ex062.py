print('Gerador de PA')
print('-='*20)
primeiro = int(input('Digite o Primeiro termo: '))
razao = int (input('Digite a Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont != total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))

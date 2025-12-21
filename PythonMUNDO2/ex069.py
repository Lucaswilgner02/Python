tot18 = toth = totf = 0
while True:
    idade = int(input('Digite sua idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('digite o sexo [M/F]: ')).strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            toth += 1
        if sexo == 'F' and idade <= 20:
            totf += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('~'* 30)
print(f'temos o total de {tot18} pessoas com mais de 18 anos cadastradas.')
print(f'{toth} Homens cadastrados')
print(f'E {totf} Mulheres com menos de 20 anos')

galera = list()
soma = media = 0
while True:
    pessoa = {}  # CORREÇÃO: Inicializa 'pessoa' como um DICIONÁRIO vazio

    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':  # CORREÇÃO: Permite 'M' ou 'F'
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':  # CORREÇÃO: Permite 'S' ou 'N'
            break
        print('ERRO! Por favor, digite apenas S ou N.')

    if resp == 'N':
        break

print('-=' * 30)

# PARTE A e B
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')

# PARTE C: Listar APENAS as mulheres cadastradas
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()

# PARTE D: Listar as pessoas com idade acima da média
print(f'D) Lista das pessoas que estão acima da média de idade:')
for p in galera:
    # A sua condição original aqui era sobre a idade, e não sobre o sexo
    if p['idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('<< ENCERRADO >>')

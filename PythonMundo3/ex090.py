aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno ['media'] = float(input(f'Media de {aluno["nome"]}: '))
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A Média é igual a {aluno["media"]}')
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'EM RECUPERAÇÃO'
else:
    aluno['situacao'] = 'REPROVADO'
for k, v in aluno.items():
    print(f' - {k} é {v}')







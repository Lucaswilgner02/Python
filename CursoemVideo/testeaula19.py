'''pessoas = {'nome': "Gustavo",'idade': 22,'sexo':'M'}
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())'''

#estado = {}
#brasil = []

'''estado1 = {'UF':"São Paulo",'Sigla':'SP'}
estado2 = {'UF':"Rio de Janeiro",'Sigla':'RJ'}
for k, v in estado1.items():
    print(f'{k} = {v}')'''

estado = {}
brasil = []
for c in range(1,4):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    estado.clear()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
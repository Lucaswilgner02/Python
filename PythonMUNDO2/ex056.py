somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('~~~~~~~~~ {}ª PESSOA ~~~~~~~~'.format(p))
    nome = str(input('NOME:')).strip()
    idade = int(input('IDADE:'))
    sexo =  str(input('SEXO M/F:')).strip()
    somaidade += idade
    if p == 1 and sexo in'Mm':
        maioridade += 1
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
        somaidade = idade
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('o Homem mais velho do grupo tem {} anos e se chama {}'.format(maioridade, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

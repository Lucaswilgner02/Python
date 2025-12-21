listagem = ('Aprender','Programar','linguagem','Python',
            'Curso','Gratis','Estudar','Praticar','Trabalhar',
            'Mercado','Programador','Futuro')
for p in listagem:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

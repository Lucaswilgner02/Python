from time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
opçao = 0
while opçao != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do sistema
    ''')
    opçao = int(input('>>>>> Qual é sua opção?'))
    if opçao == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opçao == 2:
         mult = n1 * n2
         print('{} x {} = {}'.format(n1, n2, mult))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('O maior entre {} e {} é {}'.format(n1, n2, maior))
    elif opçao == 4:
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
    elif opçao == 5:
        print('Saindo do sistema...')
    else:
        print('Opção Invalida!')
    print('=-='*10)
    sleep(2)
print('Fim do programa!, Volte sempre :)')


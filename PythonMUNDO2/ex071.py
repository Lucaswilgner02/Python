print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedula = 50  # Começamos com a maior cédula disponível (R$ 50)
total_cedulas = 0

while True:
    if total >= cedula:
        # Se o valor total for maior ou igual à cédula atual:
        # 1. Subtrai a cédula do total
        total -= cedula
        # 2. Conta que uma cédula foi usada
        total_cedulas += 1
    else:
        # Se o valor for MENOR que a cédula atual, significa que:
        # 1. A contagem da cédula anterior terminou
        if total_cedulas > 0:
            # Mostra o resultado se houver alguma cédula contada
            print(f'Total de {total_cedulas} cédulas de R$ {cedula:.2f}')

        # 2. Passa para a próxima cédula (ajuste de valor da cédula)
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        # 3. Zera a contagem para a nova cédula
        total_cedulas = 0

        # 4. Condição de parada: Se o total restante for 0, o saque acabou.
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
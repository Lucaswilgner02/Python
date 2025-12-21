try:
    a= int(input('digite o numerador: '))
    b = int(input('digite o denominador: '))
    r = a / b
except ZeroDivisionError:
    print('Não é possivel dividir por 0')
except ValueError:
    print('Valores digitados não compativeis.')
except Exception as error:
    print(f'O erro encontrado foi: {error.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte Sempre')



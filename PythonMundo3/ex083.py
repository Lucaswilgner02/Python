expr = str(input('Digite a expressão'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressão esta valida')
else:
    print('sua expressão esta invalida')
print('-='*30)

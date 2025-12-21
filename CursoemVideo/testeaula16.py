lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim','Batata frita')
print(sorted(lanche))
for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('comi pra caramba')
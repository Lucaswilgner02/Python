def lin():
    print('-='*30)
def area(larg, comp):
    area = larg * comp
    print(f'A area de um terreno de {larg} X {comp} é de {area} M²')

lin()
print('Controle de terrenos')
lin()

larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
lin()
area(larg, comp)
lin()

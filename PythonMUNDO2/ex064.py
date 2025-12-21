n=0
c=0
cont = 0
num = int(input('Digite um numero [999 PARA PARAR]: '))
while num != 999:
    if num != 999:
        c += num + n
        cont += 1
        num = int(input('Digite um numero [999 PARA PARAR]: '))
print('Você digitou {} numeros e a soma entre eles é de {}'.format(cont,c))


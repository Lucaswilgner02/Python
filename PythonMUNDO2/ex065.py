soma = quant = media = 0
pg = 'nN'
while pg not in 'Nn':
    num = int(input('Digite um numero:'))
    soma += num
    quant+= 1
    if quant == 1:
       maior = menor = num
    else:
        if num > maior:
           maior = num
        if num < menor:
           menor = num
    pg = str(input('Quer continuar?'))
media = soma/quant
print('Você digitou {} numeros e a média foi {}'.format(quant,media))
print('e o maior valor foi o {} e o menor foi {}'.format(maior,menor))







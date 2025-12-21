print('=='*20)
print('Analisador de triangulos')
print('=='*20)
r1=float(input('Primeiro segmento:'))
r2=float(input('Segundo segmento:'))
r3=float(input('Terceiro segmento:'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os seguimentos a cima não podem formar um triangulo')


a=int(input('Primeiro numero:'))
b=int(input('Segundo numero:'))
c=int(input('Terceiro numero:'))
#Verificando quem é menor
menor=a
if b<a and b<c:
   menor=b
if c<a and c<b:
    menor=c
print('O menor valor digitado foi {}'.format(menor))
#Verificando quem é maior
maior=a
if b<a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O maior valor digitado foi {}'.format(maior))

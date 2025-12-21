n=int(input('digite um numero'))
d=n*2
t=n*3
r=n**(1/2)
print('O dobro de {} vale {}.\nO triplo de {} vale{}.\nA raiz quadrada de {} é igual a {}'.format(n,d,n,t,n,r))
n=int(input('digite outro'))
print('O dobro de {} é {}.\nO triplo de {} é {}.\nA raiz quadrada de {} é {}.'.format(n,n*2,n,n*3,n,pow(n,(1/2))))
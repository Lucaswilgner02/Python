p=float(input('Digite sua primeira nota: '))
s=float(input('Digite sua segunda nota: '))
m= (p+s)/2
print('Tirando {:.1f} e {:.1f}sua media é {}'.format(p,s,m))
if m >= 7.5:
    print('\033[0;32mAPROVADO !')
elif m >= 5 and m < 7:
    print('\033[0;33mVOCÊ ESTA DE RECUPERAÇÃO!')
elif m < 5:
    print('\033[0:31mREPROVADO!')
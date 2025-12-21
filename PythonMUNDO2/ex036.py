vc=float(input('Digite o valor da casa:'))
s=float(input('Qual é o seu salário:'))
f=int(input('Quantos anos de financiamento:'))
p= vc/ (f*12)
m= s*30/100
print('Para pagar uma casa de: {:.2f} em: {:.2f} anos a prestação sera de: {:.2f} por mês'.format(vc,f,p))
if p<m:
    print('\033[0;32mEmprestimo Aprovado\033[m')
else:
    print('\033[0;31mEmprestimo Reprovado')

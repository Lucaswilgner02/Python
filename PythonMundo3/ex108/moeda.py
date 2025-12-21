def dobro (n):
   return n * 2


def triplo (n):
   return n * 3


def metade(n):
    return n / 2


def aumentar(n):
    return n+(n*10/100)


def diminuir(n):
    return n-(n*13/100)


def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:>8.2f}'.replace('.', ',')
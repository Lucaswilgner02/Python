def aumentar(preco=0, taxa=0, formatar=False):
    """
    Calcula o aumento percentual de um valor.
    :param preco: O preço inicial.
    :param taxa: A porcentagem de aumento (ex: 10 para 10%).
    :param formatar: (Opcional) Indica se o valor de retorno deve ser formatado como moeda.
    :return: O valor com o aumento aplicado, formatado ou não.
    """
    res = preco + (preco * taxa / 100)
    return res if not formatar else moeda(res)


def diminuir(preco=0, taxa=0, formatar=False):
    """
    Calcula a redução percentual de um valor.
    :param preco: O preço inicial.
    :param taxa: A porcentagem de redução (ex: 13 para 13%).
    :param formatar: (Opcional) Indica se o valor de retorno deve ser formatado como moeda.
    :return: O valor com a redução aplicada, formatado ou não.
    """
    res = preco - (preco * taxa / 100)
    return res if not formatar else moeda(res)


def dobro(preco=0, formatar=False):
    """
    Calcula o dobro de um valor.
    :param preco: O preço inicial.
    :param formatar: (Opcional) Indica se o valor de retorno deve ser formatado como moeda.
    :return: O dobro do valor, formatado ou não.
    """
    res = preco * 2
    return res if not formatar else moeda(res)


def metade(preco=0, formatar=False):
    """
    Calcula a metade de um valor.
    :param preco: O preço inicial.
    :param formatar: (Opcional) Indica se o valor de retorno deve ser formatado como moeda.
    :return: A metade do valor, formatado ou não.
    """
    res = preco / 2
    return res if not formatar else moeda(res)


def moeda(preco=0, simbolo='R$'):
    """
    Formata um valor numérico como preço em Reais (R$).
    :param preco: O valor numérico a ser formatado.
    :param simbolo: O símbolo da moeda (opcional, padrão 'R$').
    :return: A string do valor formatado.
    """
    # Formatação padrão brasileira (duas casas decimais e vírgula como separador decimal)
    return f'{simbolo} {preco:.2f}'.replace('.', ',')


def resumo(preço=0,taxaa=10,taxar=5):
    print('=' * 30)
    print('RESUMO DO VALOR')
    print('=' * 30)
    print(f'Preço analisando \t{moeda(preço)}')
    print(f'O dobro do preço \t{dobro(preço, True)}')
    print(f'Metade do preço \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de reducao: \t{diminuir(preço, taxar, True)}')
    print('=' * 30)
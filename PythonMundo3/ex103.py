def ficha(nome='<desconhecido>', gols=0):
    """
    Exibe a ficha de um jogador.

    :param nome: Nome do jogador (opcional).
    :param gols: Número de gols marcados (opcional).
    """
    print(f'O jogador {nome} fez {gols} gol(s).')

# 1. Recebe a entrada como STRING (por padrão)
n = str(input('Digite o nome do jogador: '))
g = str(input('Numero de gols: '))

# 2. **Valida o número de gols ANTES de tentar converter**
# Se a string 'g' for numérica, converte. Se não for, define 'g' como 0.
if g.isnumeric():
    g = int(g)
else:
    g = 0

# 3. Chama a função corretamente, tratando nome vazio
# Se o nome for vazio (''), usa o argumento nomeado 'gols' (e o nome padrão será '<desconhecido>').
if n.strip() == '':
    ficha(gols=g)
# Se o nome não for vazio, passa o nome e os gols como argumentos posicionais.
else:
    ficha(n, g)

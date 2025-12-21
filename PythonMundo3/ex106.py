from time import sleep

# --- Definição das Funções de Cores ---

# Códigos ANSI (padrão)
# Cores podem ser ajustadas se não funcionarem no seu terminal
C_VERMELHO = '\033[0;31m'
C_VERDE = '\033[0;32m'
C_AMARELO = '\033[0;33m'
C_AZUL = '\033[0;34m'
C_FIM = '\033[m'  # Voltar à cor padrão


def titulo(texto, cor):
    """Exibe um texto centralizado com uma cor de fundo (simulação de título)."""
    tamanho = len(texto) + 4
    print(cor, end='')
    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)
    print(C_FIM, end='')
    sleep(0.5)


def ajuda(comando):
    """Acessa e exibe o Interactive Help do Python."""
    # Título do manual em AZUL
    titulo(f' Acessando o manual do comando "{comando}"', C_AZUL)

    # Exibir a ajuda em VERDE
    print(C_VERDE, end='')
    help(comando)
    print(C_FIM, end='')
    sleep(1)


# --- Programa Principal (PyHELP) ---

comando = ''
while True:
    # Título principal do sistema em AMARELO
    titulo('SISTEMA DE AJUDA PyHELP', C_AMARELO)

    comando = input("Função ou Biblioteca (ou FIM para sair): ").strip().lower()

    if comando == 'fim':
        break  # Sai do loop

    ajuda(comando)

# Mensagem de encerramento em VERMELHO
titulo('ATÉ LOGO!', C_VERMELHO)
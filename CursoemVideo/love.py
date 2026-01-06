from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
linha = '*-*' * 15


while True:
    placar_jogador = 0
    placar_computador = 0
    placar_empate = 0
    rodada = 1
    
    print('Vamos melhor de 3, Quem vencer 2 RODADAS primeiro VENCE!!\n')

    while placar_jogador < 2 and placar_computador < 2:
        print(f'\nRodada {rodada}')
        print(''' \nSuas Opções:
      [ 0 ]Pedra
      [ 1 ]Papel
      [ 2 ]Tesoura
      [ 3 ]SAIR DO JOGO''' )
        print(linha)
        
        try:
            jogador = int(input('Qual é sua jogada?'))
        except ValueError:
            print('escolha um número valido!')
            continue
    
        if jogador == 3:
         print('\nSaindo Do Jogo!... Obrigado Volte Sempre!')
         print(linha)
         exit()

        if jogador <0 or jogador >3:
            print('Escolha uma opção VALÍDA!!! (0 A 2)')
            continue
    
        computador = randint(0,2)
   
        print('JO')
        sleep(0.5)
        print('KEN')
        sleep(0.5)
        print('PO!!!')
        print(linha)
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print(linha)
   

        if jogador == computador:
            print('Empate!')
            placar_empate += 1
            print(linha)


        elif(jogador == 0 and computador == 2) or \
            (jogador == 1 and computador == 0) or \
            (jogador == 2 and computador == 1):
            print('Jogador Venceu!\n')
            placar_jogador += 1
            print('-='*15)


        else:
            print('Computador Venceu!\n')
            placar_computador += 1
            print(linha)


        print(f'Player {placar_jogador} X {placar_computador} CPU || {placar_empate} Empates')
        rodada +=1
        print(linha)
    if placar_jogador == 2:
        print('\n 🎉🎉🎉 PARABÉNS VOCÊ GANHOU A MELHOR DE 3! 🎉🎉🎉')
        sleep(1)
    else: 
        print('\n😢😢😢 COMPUTADOR GANHOU A MELHOR DE 3 😢😢😢')
        sleep(1)
    print(linha)

    jogar_novamente = input('\n Quer jogar novamente ? (S/N)').lower()
    if jogar_novamente == 's':
        continue
        print(linha)

    else:
        print('Obrigado por Jogar!')
        break
print(linha)
    
        


     


 


def game_ppt():
    #Apresentação do jogo#
    print('-'*46)
    print('    |Pedra, Papel e Tesoura (2 JOGADORES)|    ')
    print('-'*46)
    print('\n             |PAINEL DE JOGADAS|                  ')
    print('1ª - Pedra')
    print('2ª - Papel')
    print('3ª - Tesoura')

    #Coleta de dados#
    jogadas = ('pedra', 'papel', 'tesoura')
    
    inicio_jogador1 = input('\nFaça sua jogada: ')
    inicio_jogador2 = input('Faça sua jogada: ')

    #Conversão da entrada e impressão das jogadas para letras minúsculas e sem espaços em branco sobrando.
    jogador_1 = str(inicio_jogador1.lower().strip())
    jogador_2 = str(inicio_jogador2.lower().strip())

    print(f'\n[Jogador 1]  - {jogador_1}')
    print(f'[Jogador 2] - {jogador_2}')

    #Lógica para erro de digitação
    if jogador_1 not in jogadas or jogador_2 not in jogadas:
        print('\nJogada inválida! Digite apenas "Pedra", "Papel" ou "Tesoura".')
        return
        
    #Lógica para saber se houve um empate.
    if jogador_1 == jogador_2:
        print('\nHOUVE um EMPATE!')
        return

    #Variável para receber o vencedor
    vencedor = None
    
    #Lógica para saber quem é o vencedor
    if (jogador_1 == 'pedra' and jogador_2 == 'tesoura') or \
       (jogador_1 == 'tesoura' and jogador_2 == 'papel') or \
       (jogador_1 == 'papel' and jogador_2 == 'pedra'):
        vencedor = 'jogador 1'
        print(f'\n{vencedor} venceu!!')
    else:
        vencedor = 'jogador 2'
        print(f'\n{vencedor} venceu!!')
    
    


game_ppt()

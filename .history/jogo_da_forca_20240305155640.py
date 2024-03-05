import random
import testes
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_hangman(chances):
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0 (inicial)
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def display_menu():
    print('''
    Bem-vindo(a) ao jogo da forca!
    Adivinhe o nome do filme!
    1 - jogar
    2 - adicionar filme
    3 - ver filmes
    4 - sair do jogo
    ''')
    
def jogar(palavra, palavra_escondida, chances, letras_erradas, dicas, vez):
    while chances > 0:
        # print

        print(display_hangman(chances))

        print(''.join(palavra_escondida))
        print(f'\nChances restantes: {chances}')
        print('Letras erradas', " ".join(letras_erradas))

        # input
        tentativa = input('Digite uma letra: ').lower()

        # condicional teste letras
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    palavra_escondida[index] = letra
                index += 1
            if ''.join(palavra_escondida) == palavra:
                print(''.join(palavra_escondida))
                print('Parabéns! Você ganhou!')
                break
        else:
            if tentativa in letras_erradas:
                print('Você já tentou essa letra!')
            elif tentativa == 'dica':
                print(dicas[vez]) if vez < 3 else print('Você usou todas as dicas!')
                vez += 1
            else:
                letras_erradas.append(tentativa)
            chances -= 1
                  
    if chances == 0:
        print('Você perdeu!')
        print(f'A filme era: {palavra}')

def jogo():

    limpa_tela()
    display_menu()
    
    # lista de filmes
    filmes = ['la la land', 'the handmaiden', 'scream', 'poor things']
    
    # dicas dos filmes
    infos = {'la la land': ['2016','Damien Chazelle','emma stone, ryan gosling'], 'the handmaiden': ['2016', 'Park Chan-wook', 'Kim Min-hee, Ha Jung-woo, Cho Jin-woong'], 'scream': ['1996', 'Wes Craven', 'Neve Campbell, Courteney Cox, David Arquette'], 'poor things': ['2023', 'Yorgos Lanthimos', 'Emma Stone, Mark Ruffalo, Willem Dafoe']}

    palavra = random.choice(filmes)
    palavra = palavra.lower()

    dicas = infos[palavra]
    vez = 0

    palavra_escondida = ['_' if letra != ' ' else ' ' for letra in palavra ] # operador ternario e comprehension list
    print(palavra_escondida)
    chances =  6
    letras_erradas = []

    opcao = input('Digite uma opção: ')
    if opcao == '1':
        print('jogar\n')
        jogar(palavra, palavra_escondida, chances, letras_erradas, dicas, vez)

    elif opcao == '2':
        print('adicione um filme\n')
        infoFilme = testes.filmeInfo()
        filmes.append(infoFilme[0].lower())
        infos[infoFilme[0].lower()] = [infoFilme[1],infoFilme[2],infoFilme[3]]
    elif opcao == '3':
        print('lista de filmes\n')
        for filme in filmes:
            print(filme)   
    elif opcao == '4':
        print('saindo do jogo...')
        exit()
    
  


if __name__ == "__main__":
    jogo()

    
    
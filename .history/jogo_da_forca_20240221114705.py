import random
from os import system, name

# Função para limar a tela a cada execução
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def jogo():

    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe o nome do filme!\n")

    # lista de filmes
    filmes = ['la la land', 'the handmaiden', 'scream', 'poor things', '']
    
    # dicas dos filmes
    dicas = {'la la land': ['Genero: musical','Ano: 2016','diretor: Damien Chazelle'], 'the handmaiden': ['Genero: drama','Ano: 2016','diretor: Park Chan-wook'], 'scream': ['Genero: terror','Ano: 1996','diretor: Wes Craven'], 'poor things': ['Genero: comédia','Ano: 2023','diretor: Yogors Lanthimos']}

    palavra = random.choice(filmes)
    dicasvez = dicas[palavra]
    palavra = palavra.upper()

    palavra_escondida = ['_' for letra in palavra]




    
    
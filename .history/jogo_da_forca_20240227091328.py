import random
from os import system, name

def jogo():

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe o nome do filme!\n")

    # lista de filmes
    filmes = ['la la land', 'the handmaiden', 'scream', 'poor things', '']
    
    # dicas dos filmes
    dicas = {'la la land': ['Genero: musical','Ano: 2016','diretor: Damien Chazelle'], 'the handmaiden': ['Genero: drama','Ano: 2016','diretor: Park Chan-wook'], 'scream': ['Genero: terror','Ano: 1996','diretor: Wes Craven'], 'poor things': ['Genero: comédia','Ano: 2023','diretor: Yogors Lanthimos']}

    palavra = random.choice(filmes)
    dicasvez = dicas[palavra]
    palavra = palavra
    palavra_escondida = ['_' for letra in palavra]

    chances =  10

    letras_erradas = []

    while chances > 0:
        # print
        print(' '.join(palavra_escondida))
        print(f'\nChances restantes: {chances}')
        print('Letras erradas', " ".join(letras_erradas))

        # input
        tentativa = input('Digite uma letra: ').lower()

        # condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    palavra_escondida[index] = letra
                index += 1

        else:
            chances -= 1
            letras_erradas.append(tentativa)





jogo()
    
    
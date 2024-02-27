import random
from os import system, name

# Função para limpar a tela a cada execução
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
    filmes = ['la la land', 'the handmaiden', 'scream', 'poor things']
    
    # dicas dos filmes
    info = {'la la land': ['Genero: musical','Ano: 2016','diretor: Damien Chazelle'], 'the handmaiden': ['Genero: drama','Ano: 2016','diretor: Park Chan-wook'], 'scream': ['Genero: terror','Ano: 1996','diretor: Wes Craven'], 'poor things': ['Genero: comédia','Ano: 2023','diretor: Yogors Lanthimos']}

    palavra = random.choice(filmes)
    palavra = palavra.lower()

    dicas = info[palavra]
    vez = 0

    palavra_escondida = ['_' if letra != ' ' else ' ' for letra in palavra ] # operador ternario e comprehension list
    print(palavra_escondida)
    chances =  10

    letras_erradas = []

    while chances > 0:
        # print
        print(''.join(palavra_escondida))
        print(f'\nChances restantes: {chances}')
        print('Letras erradas', " ".join(letras_erradas))

        # input
        tentativa = input('Digite uma letra: ').lower()

        # condicional teste letras
        if tentativa in palavra and tentativa != 'dica':
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
            chances -= 1
            letras_erradas.append(tentativa)
        
        # dicas 
        if tentativa == 'dica':
            print(dicas[vez])
            vez += 1
        else:
            print('Você usou todas as dicas!')
               
        

        


    if chances == 0:
        print('Você perdeu!')
        print(f'A filme era: {palavra}')
    
    




if __name__ == "__main__":
    jogo()

    
    
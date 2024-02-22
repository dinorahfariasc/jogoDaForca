#5, inverta os caracteres de uma string


string = input("Digite uma string: ")

def inverte_string(string):
    novaString = ''
    tamanho = len(string)
    for i in range(tamanho-1, -1, -1):
        novaString += string[i]

    return novaString


print(inverte_string(string))
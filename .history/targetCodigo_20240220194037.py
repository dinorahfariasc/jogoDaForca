# 2, recebe um numero e calcula a sequencia de fibonacci até o numero informado, informando se ele pertence ou nao a sequencia

num = int(input("Digite um número: "))

def fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a+b
    if b == num:
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")

fibonacci(num)

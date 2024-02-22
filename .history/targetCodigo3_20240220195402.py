# 3, calcule eretorne, menor e maior faturamento, numero de dias que tiveram faturamento acima da media

import pandas as pd

# lendo dados 
faturamentos = pd.read_json('dados.json')
faturamentos = faturamentos[faturamentos['valor'] ! = 0]
print(faturamentos)
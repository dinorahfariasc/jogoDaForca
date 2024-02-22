# 3, calcule eretorne, menor e maior faturamento, numero de dias que tiveram faturamento acima da media

import numpy as np
import pandas as pd

# lendo dados 
faturamentos = pd.read_json('dados.json')
#excluindo linhas com valores nulos
faturamentos = faturamentos.replace(0, np.nan)
faturamentos.dropna(inplace=True)

media = faturamentos['valor'].mean()
print(faturamentos,media)
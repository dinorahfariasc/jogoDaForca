# 4, calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

fatuEstados = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros':19849.53}

total = sum(fatuEstados.values())
percentual = {estado: round((faturamento/total)*100,2) for estado, faturamento in fatuEstados.items()}
print(percentual)
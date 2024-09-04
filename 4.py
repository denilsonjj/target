def calcular_percentual(faturamento):
    total = sum(faturamento.values())
    percentual = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    return percentual

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

percentuais = calcular_percentual(faturamento)
for estado, percent in percentuais.items():
    print(f"{estado}: {percent:.2f}%")

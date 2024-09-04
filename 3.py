data = {
    "faturamento_diario": [12000, 0, 15000, 11000, 18000, 0, 20000, 13000, 0, 16000]
}

def analisar_faturamento(dados):
    faturamento = dados['faturamento_diario']
    
    faturamento = [f for f in faturamento if f > 0]
    
    if not faturamento:
        return "Não há dados de faturamento disponíveis."
    
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media_faturamento = sum(faturamento) / len(faturamento)
    
    dias_acima_media = sum(1 for f in faturamento if f > media_faturamento)
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media
    }

resultado = analisar_faturamento(data)
print(resultado)

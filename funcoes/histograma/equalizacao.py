import numpy as np
from numpy.typing import NDArray

def equalizar_histograma(matriz: NDArray):
    linhas, colunas = matriz.shape    
    nova_matriz = np.zeros((linhas, colunas), dtype=np.uint8)
    
    niveis_de_cinza = {x: 0.0 for x in range(0, 256)}

    for i in range(linhas):
        for j in range(colunas):
            niveis_de_cinza[matriz[i][j]] += 1 

    niveis_frequencia = {x: (niveis_de_cinza[x] / (linhas * colunas)) for x in range(0, 256)}
    frequencia_acumulada = {}
    soma_atual = 0.0
    equalizada = {}

    for i in range(0, 256):
        soma_atual += niveis_frequencia[i]
        frequencia_acumulada[i] = soma_atual
        equalizada[i] = int(round(frequencia_acumulada[i] * 255))

    for i in range(linhas): 
        for j in range(colunas): 
            tom_original = matriz[i][j]
            nova_matriz[i][j] = equalizada[tom_original]

    print(f"Maior valor original: {np.max(matriz)}")
    print(f"Maior valor equalizado: {np.max(nova_matriz)}") # DEVE SER 255

    return nova_matriz
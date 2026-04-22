import numpy as np
from numpy.typing import NDArray

def inverter_intensidade(matriz: NDArray):
    linhas, colunas = matriz.shape
    matriz_invertida = np.zeros((linhas, colunas), dtype=np.uint8)

    for i in range(linhas):
        for j in range(colunas):
            matriz_invertida[i][j] = 255 - matriz[i][j]

    return matriz_invertida
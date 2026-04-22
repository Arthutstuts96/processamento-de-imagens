import math

import numpy as np
from numpy.typing import NDArray


def ampliar_vizinho_proximo(matriz: NDArray) -> NDArray: 
    """
    Amplia uma matriz NumPy usando a interpolação de vizinho mais próximo.
    """
    linhas = matriz.shape[0]
    colunas = matriz.shape[1]
    nova_matriz = np.zeros((linhas * 2, colunas * 2), dtype=np.uint8)

    for i in range(linhas): 
        for j in range(colunas):
            pixel = matriz[i][j]

            _i = i * 2
            _j = j * 2

            nova_matriz[_i][_j] = pixel 
            nova_matriz[_i][_j + 1] = pixel 
            nova_matriz[_i + 1][_j] = pixel 
            nova_matriz[_i + 1][_j + 1] = pixel 

    return nova_matriz

def reduzir_vizinho_proximo(matriz: NDArray):
    """
    Reduz uma matriz NumPy usando a interpolação de vizinho mais próximo.
    """
    linhas = matriz.shape[0]
    colunas = matriz.shape[1]

    nova_linhas = math.ceil(linhas / 2)
    nova_colunas = math.ceil(colunas / 2)
    nova_matriz = np.zeros((nova_linhas, nova_colunas), dtype=np.uint8)

    for i in range(0, linhas, 2): 
        for j in range(0, colunas, 2):
            pixel = matriz[i, j]

            _i = i // 2
            _j = j // 2

            nova_matriz[_i, _j] = pixel

    return nova_matriz
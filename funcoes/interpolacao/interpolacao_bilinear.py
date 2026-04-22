import numpy as np
from numpy.typing import NDArray


def ampliar_bilinear(matriz: NDArray):
    """
    Amplia uma matriz NumPy usando a interpolação bilinear.
    """
    linhas, colunas = matriz.shape
    nova_matriz = np.zeros((linhas * 2, colunas * 2), dtype=np.uint8)

    for i in range(linhas-1): 
        for j in range(colunas-1):
            pixel1 = matriz[i][j]
            pixel2 = matriz[i][j + 1]
            pixel3 = matriz[i + 1][j]
            pixel4 = matriz[i + 1][j + 1]

            _i = i * 2
            _j = j * 2

            nova_matriz[_i, _j] = pixel1
            nova_matriz[_i, _j + 1] = (pixel1 + pixel2) // 2
            nova_matriz[_i + 1, _j] = (pixel1 + pixel3) // 2
            nova_matriz[_i + 1, _j + 1] = (pixel1 + pixel2 + pixel3 + pixel4) // 4
            nova_matriz[_i + 1, _j + 2] = (pixel2 + pixel4) // 2            
            nova_matriz[_i + 2, _j + 1] = (pixel3 + pixel4) // 2

    return nova_matriz
def reduzir_bilinear(matriz: NDArray):
    """
    Reduz uma matriz NumPy usando a interpolação bilinear.
    """
    linhas, colunas = matriz.shape
    nova_matriz = np.zeros((linhas // 2, colunas // 2), dtype=np.uint8)

    for i in range(0, linhas - 1, 2):
        for j in range(0, colunas - 1, 2):
            pixel1 = matriz[i][j]
            pixel2 = matriz[i][j + 1]
            pixel3 = matriz[i + 1][j]
            pixel4 = matriz[i + 1][j + 1]

            nova_matriz[i // 2, j // 2] = (pixel1 + pixel2 + pixel3 + pixel4) // 4

    return nova_matriz
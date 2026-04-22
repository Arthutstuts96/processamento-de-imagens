import numpy as np
from numpy.typing import NDArray


def somar_matrizes(matriz_1: NDArray, matriz_2: NDArray):
    if len(matriz_1) != len(matriz_2):
        raise Exception("Matrizes com tamanhos diferentes")
    
    linhas, colunas = matriz_1.shape
    matriz_soma = np.zeros((linhas, colunas), dtype=np.uint8)

    for i in range(linhas):
        for j in range(colunas):
            soma = (matriz_1[i][j] + matriz_2[i][j]) / 2
            matriz_soma[i][j] = soma

    return matriz_soma


def subtrair_matrizes(matriz_1: NDArray, matriz_2: NDArray):
    if len(matriz_1) != len(matriz_2):
        raise Exception("Matrizes com tamanhos diferentes")
    
    linhas, colunas = matriz_1.shape
    matriz_soma = np.zeros((linhas, colunas), dtype=np.uint8)

    for i in range(linhas):
        for j in range(colunas):
            subtracao = matriz_1[i][j] - matriz_2[i][j]
            matriz_soma[i][j] = subtracao

    return matriz_soma
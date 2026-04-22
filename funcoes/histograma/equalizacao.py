from functools import reduce
import math

import numpy as np
from numpy.typing import NDArray


def equalizar_histograma(matriz: NDArray):
    linhas, colunas = matriz.shape
    nova_matriz = np.zeros((linhas // 2, colunas // 2), dtype=np.uint8)
    niveis_de_cinza = {x: 0.0 for x in range(0, 256)}

    for i in range(0, linhas - 1):
        for j in range(0, colunas - 1):
            # Para cada pixel, salvar a quantidade de cada cor para cada nível (0 a 255)
            niveis_de_cinza[matriz[i][j]] += 1 

    # Dividir cada nivel de cinza pelo numero de pixels para obter a frequência
    niveis_frequencia = {x: (niveis_de_cinza[x] / (linhas * colunas)) for x in range(0, 256)}
    frequencia_acumulada = {}
    soma_atual = 0.0

    for i in range(0, 256):
        # Soma a probabilidade do tom atual com tudo o que já passou
        soma_atual += niveis_frequencia[i]
        frequencia_acumulada[i] = soma_atual

    frequencia_acumulada[255] = math.ceil(frequencia_acumulada[255])

    equalizada = {}

    for i in range(0, 256):
        # Soma a probabilidade do tom atual com tudo o que já passou
        equalizada[i] = frequencia_acumulada[i] * 255

    for i in range(0, linhas - 1):
        for j in range(0, colunas - 1):
            matriz[i][j] = equalizada[matriz[i][j]] 

    return nova_matriz
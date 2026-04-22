from numpy.typing import NDArray
import numpy as np
import math


def rotacionar_matriz(matriz: NDArray, angulo: float):
    a = math.radians(-angulo)
    matriz_rotacao = np.matrix(([[math.cos(a), -math.sin(a), 0],
                                [math.sin(a), math.cos(a), 0],
                                [0, 0, 1]]))
    
    linhas, colunas = matriz.shape
    matriz_resultado = np.zeros((linhas, colunas), dtype=np.uint8)

    centro_i = linhas // 2
    centro_j = colunas // 2

    for i in range(linhas):
        for j in range(colunas):
            x_relativo = j - centro_j
            y_relativo = i - centro_i

            pixel_matriz_coluna = np.matrix([[x_relativo], 
                                            [y_relativo], 
                                            [1]])
        
            pos_origem = matriz_rotacao @ pixel_matriz_coluna

            _j_orig = int(pos_origem[0, 0]) + centro_j
            _i_orig = int(pos_origem[1, 0]) + centro_i
            
            if 0 <= _i_orig < linhas and 0 <= _j_orig < colunas:
                matriz_resultado[i, j] = matriz[_i_orig, _j_orig]
    
    return matriz_resultado
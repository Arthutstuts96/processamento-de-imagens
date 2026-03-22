from numpy.typing import NDArray


def ampliar_vizinho_proximo(matriz: NDArray):
    linhas = matriz.shape[0]
    colunas = matriz.shape[1]

    for i in range(0, 1):
        for j in range(0, 1):    
            pixel = matriz[i][j]
            print(matriz[i][j], matriz[i][j+1], matriz[i+1][j], matriz[i+1][j+1])

def reduzir_vizinho_proximo(matriz: NDArray):
    pass
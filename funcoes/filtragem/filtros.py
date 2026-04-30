import numpy as np

def aplicar_filtro(matriz, filtro="media"):
    linhas, colunas = matriz.shape    
    nova_matriz = np.zeros((linhas, colunas), dtype=np.uint8)

    #TODO: Colocar cases para os outros filtros
    match filtro:
        case "laplace-1": mascara = [[0,1,0],
                                    [1,-4,1],
                                    [0,1,0]]
            
        case "laplace-2": mascara = [[0,-1,0],
                                    [-1,4,-1],
                                    [0,-1,0]]
            
        case "laplace-3": mascara = [[1,1,1],
                                    [1,-8,1],
                                    [1,1,1]]
            
        case "laplace-4": mascara = [[-1,-1,-1],
                                    [-1,8,-1],
                                    [-1,-1,-1]]
            
        case "sobel-h": mascara = [[-1,-2,-1],
                                [0,0,0],
                                [1,2,1]]
            
        case "sobel-v": mascara = [[-1,0,1],
                                [-2,0,2],
                                [-1,0,1]]
            
        case "media": mascara = [[1,1,1],
                                [1,1,1],
                                [1,1,1]]
        case "_":
            mascara = [[1,1,1],
                    [1,1,1],
                    [1,1,1]]

    for i in range(linhas):
        for j in range(colunas):
            
            cima = (i - 1) % linhas
            baixo = (i + 1) % linhas
            esquerda = (j - 1) % colunas
            direita = (j + 1) % colunas
            
            soma = (
                int(matriz[cima][esquerda]) * mascara[0][0] + 
                int(matriz[cima][j]) * mascara[0][1] + 
                int(matriz[cima][direita]) * mascara[0][2] +
                int(matriz[i][esquerda]) * mascara[1][0] + 
                int(matriz[i][j]) * mascara[1][1] + 
                int(matriz[i][direita]) * mascara[1][2] +
                int(matriz[baixo][esquerda]) * mascara[2][0] + 
                int(matriz[baixo][j]) * mascara[2][1] + 
                int(matriz[baixo][direita]) * mascara[2][2]
            )
            
            resultado = soma / 9
            nova_matriz[i][j] = round(resultado) if resultado > 0 else abs(resultado)
            
    return nova_matriz
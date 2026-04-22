import numpy as np

def rotular_imagem(matriz):
    def tem_rotulo(valor: int):
        return valor != 0
    
    linhas, colunas = matriz.shape
    matriz_rotulos = np.zeros((linhas, colunas), dtype=int)
    
    proximo_rotulo = 1
    equivalencias = {}

    for i in range(linhas):
        for j in range(colunas):
            if not tem_rotulo(matriz[i, j]):
                cima = matriz_rotulos[i-1, j] if i > 0 else 0
                esquerda = matriz_rotulos[i, j-1] if j > 0 else 0

                if not tem_rotulo(cima) and not tem_rotulo(esquerda):
                    matriz_rotulos[i, j] = proximo_rotulo
                    equivalencias[proximo_rotulo] = proximo_rotulo
                    proximo_rotulo += 1
                    
                elif tem_rotulo(cima) and not tem_rotulo(esquerda):
                    matriz_rotulos[i, j] = cima
                elif not tem_rotulo(cima) and tem_rotulo(esquerda):
                    matriz_rotulos[i, j] = esquerda
                    
                else:
                    menor_rotulo = min(cima, esquerda)
                    maior_rotulo = max(cima, esquerda)
                    
                    matriz_rotulos[i, j] = menor_rotulo
                    
                    equivalencias[maior_rotulo] = menor_rotulo

    for rotulo in equivalencias:
        atual = rotulo
        while equivalencias[atual] != atual:
            atual = equivalencias[atual]
        equivalencias[rotulo] = atual

    rotulos_finais = {}
    for i in range(linhas):
        for j in range(colunas):
            if matriz_rotulos[i, j] != 0:
                rotulo_correto = equivalencias[matriz_rotulos[i, j]]
                
                if rotulo_correto not in rotulos_finais:
                    rotulos_finais[rotulo_correto] = []
                
                rotulos_finais[rotulo_correto].append((i, j))

    return rotulos_finais
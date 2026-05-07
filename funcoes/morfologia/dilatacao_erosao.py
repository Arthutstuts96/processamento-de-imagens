import numpy as np

def aplicar_dilatacao_erosao(matriz, operacao='dilatacao'):
    linhas, colunas = matriz.shape
    matriz_resultado = np.zeros((linhas, colunas), dtype=np.uint8)

    for i in range(linhas):
        for j in range(colunas):
            
            # Inicializamos variáveis para checar a vizinhança
            tem_branco = False  # Para Dilatação (pelo menos um 255)
            todos_brancos = True # Para Erosão (todos precisam ser 255)

            # Percorremos a vizinhança 3x3 manualmente de -1 a +1
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ni = i + di
                    nj = j + dj

                    # Verificamos se o vizinho está dentro dos limites da matriz
                    if 0 <= ni < linhas and 0 <= nj < colunas:
                        valor_vizinho = matriz[ni][nj]
                        
                        if valor_vizinho == 255:
                            tem_branco = True
                        else:
                            todos_brancos = False
                    else:
                        # Se estiver fora da borda, tratamos como 0 (preto)
                        # Isso faz a Erosão "corroer" as bordas da imagem
                        todos_brancos = False

            # Aplicação da lógica baseada na operação escolhida
            if operacao == 'dilatacao':
                if tem_branco:
                    matriz_resultado[i][j] = 255
                else:
                    matriz_resultado[i][j] = 0
                    
            elif operacao == 'erosao':
                if todos_brancos:
                    matriz_resultado[i][j] = 255
                else:
                    matriz_resultado[i][j] = 0
                    
    return matriz_resultado
import numpy as np


def calcular_histograma(matriz):
    """Calcula a frequência de cada tom de cinza na imagem."""
    linhas = len(matriz)
    colunas = len(matriz[0])
    histograma = [0] * 256 # Lista de 256 posições (0 a 255)
    
    for i in range(linhas):
        for j in range(colunas):
            valor = int(matriz[i][j])
            histograma[valor] += 1
            
    return histograma

def encontrar_limiar_vale(histograma, distancia_minima):
    """Encontra o vale entre os dois maiores picos do histograma."""
    # 1. Encontrar o primeiro pico (o tom de cinza que mais aparece)
    pico1 = 0
    max_valor1 = -1
    for i in range(256):
        if histograma[i] > max_valor1:
            max_valor1 = histograma[i]
            pico1 = i
            
    # 2. Encontrar o segundo pico (deve ter uma distância mínima do pico 1)
    # A distância evita que o algoritmo pegue um pico adjacente da mesma "montanha"
    pico2 = 0
    max_valor2 = -1
    
    for i in range(256):
        if abs(i - pico1) >= distancia_minima:
            if histograma[i] > max_valor2:
                max_valor2 = histograma[i]
                pico2 = i
                
    # 3. Encontrar o vale (menor valor entre o pico 1 e o pico 2)
    inicio = min(pico1, pico2)
    fim = max(pico1, pico2)
    
    vale = inicio
    min_frequencia = histograma[inicio]
    
    for i in range(inicio, fim + 1):
        if histograma[i] < min_frequencia:
            min_frequencia = histograma[i]
            vale = i
            
    return vale

def segmentacao_por_vale(matriz: np.ndarray, distancia_minima=40) -> np.ndarray:
    """Função principal que aplica a limiarização e retorna um NDArray."""
    
    # Como agora garantimos que é um NDArray, podemos usar .shape
    linhas, colunas = matriz.shape
    
    # Criamos a matriz de resultado diretamente com NumPy, preenchida com 0 (preto)
    matriz_resultado = np.zeros((linhas, colunas), dtype=np.uint8)
    
    # Executa os passos do método do vale
    histograma = calcular_histograma(matriz)
    limiar = encontrar_limiar_vale(histograma, distancia_minima)
    
    print(f">> Limiar (Vale) encontrado: {limiar}")
    
    # Aplica a binarização
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i, j] > limiar:  # Acesso otimizado do NumPy [i, j]
                matriz_resultado[i, j] = 255 # Objeto (Branco)
            
            # Nota: Não precisamos mais do 'else: matriz_resultado[i, j] = 0' 
            # porque o np.zeros já inicializou tudo como 0!
                
    return matriz_resultado
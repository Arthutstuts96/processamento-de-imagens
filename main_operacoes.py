# TODO: Fazer 2 operações aritmética de adição, subtração, multiplicação ou divisão
# TODO: Fazer 1 operação geométrica de rotação, espelhamento, translação ou reflexão
# TODO: Fazer 1 operação de transformação de intensidade(negativa, logarítmica, exponencial)

from PIL import Image
from conversao import converter_para_preto_e_branco, imagem_para_matriz, salvar_matriz_como_imagem
from funcoes.operacoes.rotacao import rotacionar_matriz
from funcoes.operacoes.aritmetica import somar_matrizes, subtrair_matrizes
from funcoes.operacoes.intensidade import inverter_intensidade


def main():
    caminho_um = "imagens/resultados/filtragem/filtro_beatles_laplace_4.png"
    caminho_pb_um = "imagens/resultados/filtragem/filtro_beatles_laplace_4.png"

    try:
        imagem_um = Image.open(caminho_pb_um)
    except FileNotFoundError:
        print("Imagem não existe, convertendo...")
        imagem_um = converter_para_preto_e_branco(caminho_um)
        if imagem_um:
            imagem_um.save(caminho_pb_um)

    matriz_pixels_um = imagem_para_matriz(imagem_um)
    
    # --- SOMA
    #matriz_soma = somar_matrizes(matriz_pixels_um, matriz_pixels_dois)
    #salvar_matriz_como_imagem(matriz_soma, "operacoes/aritmetica/imagem_soma_MARIOBANANA.jpg")

    # --- SUBTRAÇÃO
    #matriz_subtracao = subtrair_matrizes(matriz_pixels_um, matriz_pixels_dois)
    #salvar_matriz_como_imagem(matriz_subtracao, "operacoes/aritmetica/imagem_subtracao_MARIOBANANA.jpg")

    # --- ROTAÇÃO
    #matriz_rotacao = rotacionar_matriz(matriz_pixels_dois, 90)
    #salvar_matriz_como_imagem(matriz_rotacao, "operacoes/geometrica/mario_90_graus.png")

    matriz_invertida = inverter_intensidade(matriz_pixels_um)
    salvar_matriz_como_imagem(matriz_invertida, "operacoes/intensidade/filtro_beatles_invertido.jpg")

if __name__ == "__main__":
    main()

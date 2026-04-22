# TODO: Fazer 2 operações aritmética de adição, subtração, multiplicação ou divisão
# TODO: Fazer 1 operação geométrica de rotação, espelhamento, translação ou reflexão

from PIL import Image
from conversao import converter_para_preto_e_branco, imagem_para_matriz, salvar_matriz_como_imagem
from funcoes.operacoes.rotacao import rotacionar_matriz
from funcoes.operacoes.aritmetica import somar_matrizes, subtrair_matrizes


def main():
    caminho_um = "imagens/banana_1.jpg"
    caminho_dois = "imagens/mario.png"
    caminho_pb_um = "imagens/preto_e_branco/banana_1.jpg"
    caminho_pb_dois = "imagens/preto_e_branco/mario.png"

    try:
        imagem_um = Image.open(caminho_pb_um)
        imagem_dois = Image.open(caminho_pb_dois)
    except FileNotFoundError:
        print("Imagem não existe, convertendo...")
        imagem_um = converter_para_preto_e_branco(caminho_um)
        imagem_dois = converter_para_preto_e_branco(caminho_dois)
        if imagem_um and imagem_dois:
            imagem_um.save(caminho_pb_um)
            imagem_dois.save(caminho_pb_dois)

    matriz_pixels_um = imagem_para_matriz(imagem_um)
    matriz_pixels_dois = imagem_para_matriz(imagem_dois)
    
    # --- SOMA
    matriz_soma = somar_matrizes(matriz_pixels_um, matriz_pixels_dois)
    salvar_matriz_como_imagem(matriz_soma, "operacoes/aritmetica/imagem_soma_MARIOBANANA.jpg")

    # --- SUBTRAÇÃO
    matriz_subtracao = subtrair_matrizes(matriz_pixels_um, matriz_pixels_dois)
    salvar_matriz_como_imagem(matriz_subtracao, "operacoes/aritmetica/imagem_subtracao_MARIOBANANA.jpg")

    # --- ROTAÇÃO
    matriz_rotacao = rotacionar_matriz(matriz_pixels_dois, 90)
    salvar_matriz_como_imagem(matriz_rotacao, "operacoes/geometrica/mario_90_graus.png")

if __name__ == "__main__":
    main()

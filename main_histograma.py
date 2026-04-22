from PIL import Image
import os

from conversao import converter_para_preto_e_branco, imagem_para_matriz, salvar_matriz_como_imagem
from funcoes.histograma.equalizacao import equalizar_histograma

def main():
    caminho = "imagens/banana.jpg"
    caminho_pb = "imagens/preto_e_branco/banana.jpg"

    try:
        imagem = Image.open(caminho_pb)
    except FileNotFoundError:
        print("Imagem não existe, convertendo...")
        imagem = converter_para_preto_e_branco(caminho)
        if imagem:
            imagem.save(caminho_pb)
   
    matriz_pixels = imagem_para_matriz(imagem)
    
    nova_imagem = equalizar_histograma(matriz_pixels)
    salvar_matriz_como_imagem(nova_imagem, "histograma/banana_equalizada.jpg")


if __name__ == "__main__":
    main()
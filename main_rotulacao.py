from PIL import Image
from conversao import binarizar_imagem, converter_para_preto_e_branco, imagem_para_matriz, salvar_matriz_como_imagem
import os

from rotulacao.rotulacao import rotular_imagem

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
    

    imagem_binaria = binarizar_imagem(matriz_pixels)
    salvar_matriz_como_imagem(imagem_binaria, "rotulacao/bananaBINARIA.jpg")
    rotulos = rotular_imagem(imagem_binaria)
    print(f"Rótulos: {rotulos}")


if __name__ == "__main__":
    main()
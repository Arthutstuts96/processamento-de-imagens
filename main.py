from PIL import Image
from conversao import converter_para_preto_e_branco, imagem_para_matriz, salvar_matriz_como_imagem
from interpolacao.interpolacao_vizinho_proximo import ampliar_vizinho_proximo, reduzir_vizinho_proximo
from interpolacao.interpolacao_bilinear import ampliar_bilinear, reduzir_bilinear
import os

def main():
    caminho = "imagens/praiadowindows.jpg"
    caminho_pb = "imagens/preto_e_branco/praiadowindows_pb.jpg"

    try:
        imagem = Image.open(caminho_pb)
    except FileNotFoundError:
        print("Imagem não existe, convertendo...")
        imagem = converter_para_preto_e_branco(caminho)
        imagem.save(caminho_pb)
   
    matriz_pixels = imagem_para_matriz(imagem)
    
    print(f"Dimensões da matriz: {matriz_pixels.shape}")

    # nova_imagem = ampliar_vizinho_proximo(matriz_pixels)
    # nova_imagem = reduzir_vizinho_proximo(matriz_pixels)
    # salvar_matriz_como_imagem(nova_imagem, "aumento_vizinho_mario.jpg")
    
    nova_imagem = ampliar_bilinear(matriz_pixels)
    salvar_matriz_como_imagem(nova_imagem, "aumento_bilinear_praiadowindows.jpg")

    nova_imagem = reduzir_bilinear(matriz_pixels)
    salvar_matriz_como_imagem(nova_imagem, "reduzido_bilinear_praiadowindows.jpg")


if __name__ == "__main__":
    main()
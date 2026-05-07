from PIL import Image
from conversao import binarizar_imagem, converter_para_preto_e_branco, imagem_para_matriz, salvar_matriz_como_imagem
from funcoes.morfologia.dilatacao_erosao import aplicar_dilatacao_erosao

def main():
    caminho = "imagens/mario.png"
    caminho_pb = "imagens/preto_e_branco/mario.png"

    try:
        imagem = Image.open(caminho_pb)
    except FileNotFoundError:
        print("Imagem não existe, convertendo...")
        imagem = converter_para_preto_e_branco(caminho)
        if imagem:
            imagem.save(caminho_pb)
   
    matriz_pixels = imagem_para_matriz(imagem)
    matriz_binaria = binarizar_imagem(matriz_pixels)
    
    nova_imagem = aplicar_dilatacao_erosao(matriz_pixels)
    salvar_matriz_como_imagem(nova_imagem, "morfologia/mario_dilatado.png")


if __name__ == "__main__":
    main()
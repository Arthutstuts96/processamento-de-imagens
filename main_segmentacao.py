from PIL import Image
from conversao import binarizar_imagem, converter_para_preto_e_branco, imagem_para_matriz, salvar_matriz_como_imagem
from funcoes.morfologia.dilatacao_erosao import aplicar_dilatacao_erosao
from funcoes.segmentacao.limiarizacao import segmentacao_por_vale

def main():
    caminho = "imagens/peach_2.jpg"
    caminho_pb = "imagens/preto_e_branco/peach_2.jpg"

    try:
        imagem = Image.open(caminho_pb)
    except FileNotFoundError:
        print("Imagem não existe, convertendo...")
        imagem = converter_para_preto_e_branco(caminho)
        if imagem:
            imagem.save(caminho_pb)
   
    matriz_pixels = imagem_para_matriz(imagem)
    
    nova_imagem = segmentacao_por_vale(matriz_pixels, distancia_minima=40)
    
    salvar_matriz_como_imagem(nova_imagem, "segmentacao/peach_2_limiarizado.jpg")

if __name__ == "__main__":
    main()
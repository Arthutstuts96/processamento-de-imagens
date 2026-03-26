import os

from PIL import Image
import numpy as np
from numpy.typing import NDArray

def converter_para_preto_e_branco(caminho_imagem):
    """
    Abre uma imagem a partir do caminho especificado e a converte para tons de cinza.
    """
    try:
        imagem = Image.open(caminho_imagem)
        imagem_pb = imagem.convert('L')
        
        return imagem_pb
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return None

def imagem_para_matriz(imagem):
    """
    Transforma um objeto de imagem do Pillow em uma matriz NumPy.
    """
    return np.array(imagem)


def salvar_matriz_como_imagem(matriz: NDArray, nome_arquivo):
    """
    Converte uma matriz NumPy em uma imagem preto e branco e salva em imagens/resultados/interpolacao.
    """
    diretorio_destino = os.path.join("imagens", "resultados", "interpolacao")
    caminho_completo = os.path.join(diretorio_destino, nome_arquivo)

    try:
        imagem_pb = Image.fromarray(matriz, mode='L')
        imagem_pb.save(caminho_completo)
        print(f"Imagem salva com sucesso em {caminho_completo}")
        
    except Exception as e:
        print(f"Erro ao salvar imagem: {e}")
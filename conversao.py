from PIL import Image
import numpy as np

def converter_para_preto_e_branco(caminho_imagem):
    """
    Abre uma imagem a partir do caminho especificado e a converte para tons de cinza.
    """
    try:
        imagem = Image.open(caminho_imagem)
        
        # O modo 'L' converte a imagem para tons de cinza (Luminância)
        # pixels vão de 0 a 255
        imagem_pb = imagem.convert('L')
        
        return imagem_pb
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return None

def imagem_para_matriz(imagem):
    """
    Transforma um objeto de imagem do Pillow em uma matriz NumPy (array 2D).
    """
    return np.array(imagem)
def rotular_imagem(matriz):
    def criterio_aceitacao(valor):
        return valor == 0
    
    linhas, colunas = matriz.shape
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rotulos = {}
    index = 0

    for i in range(linhas-1):
        for j in range(colunas-1):
            pixel = {
                "valor": matriz[i][j],
                "posicao": (i, j),
                "rotulo": ""
            }

            print(pixel)
            
            cima = {
                "valor": matriz[i-1][j],
                "posicao": (i-1, j),
                "rotulo": ""
            }
            esquerda = {
                "valor": matriz[i][j-1],
                "posicao": (i, j-1),
                "rotulo": ""
            }

            if criterio_aceitacao(pixel):
                pixel["rotulo"] = letras[index]

                # Verifica o de cima
                if criterio_aceitacao(cima):
                    print("Igual o de cima")
                    pixel["rotulo"] = cima["rotulo"]
                    rotulos[letras[index]].append(pixel)

                # Verifica o da esquerda
                elif criterio_aceitacao(esquerda):
                    print("Igual o da esquerda")
                    pixel["rotulo"] = esquerda["rotulo"]
                    rotulos[letras[index]].append(pixel)

                else:
                    print('Novo rótulo')
                    rotulos[letras[index]] = [pixel]
                    index += 1

    return rotulos

import cv2
import numpy as np
import os

# Caminho da pasta com as imagens
pasta_imagens = "path-img"

# Lista todas as imagens na pasta
imagens = os.listdir(pasta_imagens)

# Caminho onde você deseja salvar as imagens
pasta_saida = "path-saída"

# Certifique-se de que a pasta de saída exista ou crie-a se não existir
os.makedirs(pasta_saida, exist_ok=True)

# Tamanho fixo desejado para as imagens
tamanho_fixo = (500, 500)  # Ajuste o tamanho conforme necessário

# Parâmetros para adicionar espaço ao redor do rosto
margem = 300  # Ajuste a margem conforme necessário

# Carregar o classificador para detecção de rostos
classificador = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

for imagem_nome in imagens:
    if imagem_nome.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        # Carregar a imagem
        imagem = cv2.imread(os.path.join(pasta_imagens, imagem_nome))

        # Converter a imagem para escala de cinza para a detecção de rostos
        cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # Detectar rostos na imagem
        rostos = classificador.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in rostos:
            # Aumentar a região do rosto com a margem
            x -= margem
            y -= margem
            w += 2 * margem
            h += 2 * margem

            # Garantir que as coordenadas não sejam negativas
            x = max(0, x)
            y = max(0, y)

            # Recortar a região do rosto com a margem
            rosto_recortado = imagem[y:y + h, x:x + w]

            # Redimensionar o rosto mantendo a proporção original
            aspect_ratio = rosto_recortado.shape[1] / rosto_recortado.shape[0]
            new_width = int(tamanho_fixo[1] * aspect_ratio)
            roi_resized = cv2.resize(rosto_recortado, (new_width, tamanho_fixo[1]))

            # Criar uma imagem transparente com fundo transparente
            altura, largura, _ = roi_resized.shape
            mascara = np.zeros((altura, largura, 4), dtype=np.uint8)

            # Criar uma máscara circular com fundo transparente
            centro_x, centro_y = largura // 2, altura // 2
            raio = min(centro_x, centro_y)
            for i in range(altura):
                for j in range(largura):
                    if (i - centro_y) ** 2 + (j - centro_x) ** 2 <= raio ** 2:
                        mascara[i, j, :3] = roi_resized[i, j, :]

            # Definir o canal alfa (transparência) para 255 (totalmente opaco) para o rosto e 0 (totalmente transparente) para o fundo
            mascara[:, :, 3] = np.where(np.all(mascara[:, :, :3] == 0, axis=2), 0, 255)

            # Salvar a imagem com fundo transparente na pasta de saída em formato PNG
            novo_nome = os.path.join(pasta_saida, "img_" + os.path.splitext(imagem_nome)[0] + ".png")
            cv2.imwrite(novo_nome, mascara)

print("Processo concluído.")

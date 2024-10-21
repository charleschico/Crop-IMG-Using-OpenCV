# Detecção e Recorte de Imagem Usando OpenCV

Este projeto utiliza o OpenCV para realizar a detecção e recorte de rostos em imagens, com suporte para processamento em lote e geração de imagens circulares com fundo transparente.

## Características
- Detecção automática de rostos utilizando o OpenCV.
- Processamento em lote de todas as imagens em uma pasta.
- Geração de imagens circulares com fundo transparente.
- Salvamento automático das imagens processadas no formato PNG.

## Requisitos
Para utilizar este projeto, você precisará de:
- Python 3.6 ou superior.
- Pacotes listados no arquivo `requirements.txt`.

## Instalação
Para instalar as dependências e preparar o ambiente, execute os seguintes comandos:

- Clone este repositório:
```
git clone https://github.com/charleschico/Crop-IMG-Using-OpenCV.git
```
- Instale as dependências:
```
pip install -r requirements.txt
```

## Uso
Para processar as imagens, siga estes passos:
1. Coloque as imagens que deseja processar em uma pasta.
2. Execute o script principal com o comando:
```
python resizeIMG.py
```
4. As imagens recortadas serão salvas automaticamente na pasta escolhida, no formato PNG.


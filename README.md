## 🚀 Funcionalidades

- **Detecção Automática de Rostos**: Utiliza um classificador pré-treinado para localizar rostos nas imagens.
- **Margem Ajustável**: Adiciona uma margem ao redor do rosto antes do recorte.
- **Imagem Circular**: Gera uma imagem com o rosto centralizado em um círculo, removendo o fundo original.
- **Fundo Transparente**: As imagens são salvas com fundo transparente em formato PNG, ideal para perfis ou documentos.
- **Processamento em Lote**: Processa todas as imagens em uma pasta de origem e salva na mesma pasta ou em outra configurada.

---

## 🛠️ Passos Principais do Código

1. Lista todas as imagens na pasta de entrada.
2. Carrega o classificador de detecção de rostos.
3. Converte cada imagem para escala de cinza.
4. Detecta rostos nas imagens usando o classificador.
5. Aplica uma margem ao redor de cada rosto detectado.
6. Recorta a região do rosto com a margem definida.
7. Cria uma nova imagem com fundo transparente e o rosto inserido em um círculo centralizado.
8. Salva a imagem resultante em formato PNG na pasta de destino.

---

## ⚙️ Requisitos

Instale as dependências necessárias executando:

```bash
pip install -r requirements.txt
# Recorte-IMG-Usando-OpenCV

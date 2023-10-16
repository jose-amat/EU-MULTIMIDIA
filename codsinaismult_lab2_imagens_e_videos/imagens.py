from PIL import Image
import os

def redimensionar_e_salvar(input_path, output_path, nova_resolucao):
    # Abrir a imagem
    imagem = Image.open(input_path)

    # Redimensionar a imagem mantendo a mesma largura e altura
    imagem_redimensionada = imagem.resize(nova_resolucao, Image.LANCZOS)

    # Salvar a nova imagem
    imagem_redimensionada.save(output_path)

# Caminho para a pasta que contém as imagens
#caminho = "/home/frederico/2023.3/CSM/labs/lab02/imagens/camera_celular/"
caminho = "camera_celular/originais"
#caminho = "C:\Users\joamat\OneDrive - SAS\Documents\UFABC\CodSinaisMult\codsinaismult_lab2_imagens_e_videos\camera_celular\originais"

# Resolução desejada (largura, altura)
nova_resolucao = (200, 800)  # Substitua pelos valores desejados

# Iterar sobre as imagens na pasta
for filename in os.listdir(caminho):
    if filename.endswith(".mp4") or filename.endswith(".mov"):
        input_path = os.path.join(caminho, filename)
        output_path = os.path.join(caminho, "nova_resolucao_" + filename)

        redimensionar_e_salvar(input_path, output_path, nova_resolucao)

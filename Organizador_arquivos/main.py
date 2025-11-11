import os
import shutil

# Caminho da pasta que você quer organizar
import os
pasta = os.path.dirname(os.path.abspath(__file__))

# Dicionário com tipos de arquivo e destino
tipos = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Vídeos": [".mp4", ".mov", ".avi"],
    "Áudios": [".mp3", ".wav"],
    "Compactados": [".zip", ".rar"]
}

# Verifica e cria pastas
for nome_pasta in tipos.keys():
    caminho_pasta = os.path.join(pasta, nome_pasta)
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

# Move os arquivos para as pastas certas
for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)
    if os.path.isfile(caminho_arquivo):
        for nome_pasta, extensoes in tipos.items():
            if any(arquivo.lower().endswith(ext) for ext in extensoes):
                shutil.move(caminho_arquivo, os.path.join(pasta, nome_pasta, arquivo))
                print(f"Movido: {arquivo} → {nome_pasta}")
                break

"""
1. Copia as 6 fotos de barramentos para img/
2. Troca o fundo preto da máquina dessecante para branco
"""
from PIL import Image, ImageFilter
import numpy as np
import shutil, os

IMG = r"C:\Users\kauap\Documents\aepaineis-site\img"
BAR_SRC = r"C:\Users\kauap\OneDrive\Documentos\aepaineis-site\Fotos barramentos CATALOGO"

# === 1. Copiar barramentos ===
bar_map = {
    "BARRAMENTO BIFASICO .png": "barramento-cat-bifasico.png",
    "BARRAMENTO CONEXÃO VIA FIO.png": "barramento-cat-conexao-fio.png",
    "KIT BARRAMENTO COM TERMO CONEXÃO DIRETO NO CAIXA MOLDADA KIT COM NEUTRO E TERRA E TRILHOS DIN.png": "barramento-cat-kit-trifasico.png",
    "KIT BARRAMENTO NEUTRO E TERRA.png": "barramento-cat-kit-neutro-terra.png",
    "BARRAMENTO NEUTRO.png": "barramento-cat-neutro.png",
    "BARRAMENTO TERRA.png": "barramento-cat-terra.png",
}

for src_name, dst_name in bar_map.items():
    src = os.path.join(BAR_SRC, src_name)
    dst = os.path.join(IMG, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"OK: {src_name} -> {dst_name}")
    else:
        print(f"ERRO: Não encontrou {src_name}")

# === 2. Trocar fundo preto da dessecante para branco ===
maq_path = os.path.join(IMG, "maquina-enchimento-dessecante.jpg")
print(f"\nProcessando fundo da máquina dessecante...")

img = Image.open(maq_path).convert("RGB")
arr = np.array(img)

# Pixels escuros (fundo preto): R,G,B todos < 40
mask = (arr[:,:,0] < 40) & (arr[:,:,1] < 40) & (arr[:,:,2] < 40)

# Trocar para branco
arr[mask] = [255, 255, 255]

# Salvar
result = Image.fromarray(arr)
result.save(maq_path, quality=95)
print(f"Fundo trocado para branco: {maq_path}")

print("\nTudo pronto!")

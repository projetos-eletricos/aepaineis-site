"""Copia as 3 fotos da Linha DIN Sob Medida para img/"""
import shutil, os

IMG = r"C:\Users\kauap\Documents\aepaineis-site\img"
SRC = r"C:\Users\kauap\OneDrive\Documentos\aepaineis-site\Linha Din sob medida"

fotos = {
    "bifasico.webp": "din-sobmedida-bifasico.webp",
    "trifasico.webp": "din-sobmedida-trifasico.webp",
    "especial.jpg": "din-sobmedida-especial.jpg",
}

for src_name, dst_name in fotos.items():
    src = os.path.join(SRC, src_name)
    dst = os.path.join(IMG, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"OK: {src_name} -> {dst_name}")
    else:
        print(f"ERRO: {src_name}")

print("Pronto!")

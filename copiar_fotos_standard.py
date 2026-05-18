"""Copia fotos da Linha Standard para img/"""
import shutil, os

IMG = r"C:\Users\kauap\Documents\aepaineis-site\img"
SRC = r"C:\Users\kauap\OneDrive\Documentos\aepaineis-site\LINHA STANDARD"

fotos = {
    "BARRAMENTO BIFASICO 1.png": "standard-bifasico-1.png",
    "BARRAMENTO BIFASICO 2.png": "standard-bifasico-2.png",
    "barramento trifasico 1.png": "standard-trifasico-1.png",
    "barramento trifasico 2.png": "standard-trifasico-2.png",
}

for src_name, dst_name in fotos.items():
    src = os.path.join(SRC, src_name)
    dst = os.path.join(IMG, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"OK: {src_name} -> {dst_name}")
    else:
        print(f"ERRO: {src_name} nao encontrado")

print("Pronto!")

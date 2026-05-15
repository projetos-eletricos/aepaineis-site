"""
Copia as fotos das pastas de Neutro/Terra e Derivação para img/
"""
import shutil, os

IMG = r"C:\Users\kauap\Documents\aepaineis-site\img"
NT_SRC = r"C:\Users\kauap\OneDrive\Documentos\aepaineis-site\barramento neutro e terra"
DV_SRC = r"C:\Users\kauap\OneDrive\Documentos\aepaineis-site\Barramento de derivação"

# === Neutro e Terra ===
nt_map = {
    "KIT BARRAMENTO NEUTRO E TERRA.png": "bar-kit-neutro-terra.png",
    "BARRAMENTO NEUTRO.png": "bar-neutro.png",
    "BARRAMENTO TERRA.png": "bar-terra.png",
    "KIT BARRAMENTO NEUTRO E TERRA.webp": "bar-kit-neutro-terra-2.webp",
    "BARRAMENTO NEUTRO-TERRA 100A.webp": "bar-neutro-terra-100a.webp",
    "MINI BARRAMENTO NEUTRO E TERRA.webp": "bar-mini-neutro-terra.webp",
}

print("=== Copiando fotos Neutro e Terra ===")
for src_name, dst_name in nt_map.items():
    src = os.path.join(NT_SRC, src_name)
    dst = os.path.join(IMG, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"  OK: {src_name} -> {dst_name}")
    else:
        print(f"  ERRO: Nao encontrou {src_name}")

# === Derivação ===
print("\n=== Copiando fotos Derivação ===")
for i in range(1, 6):
    src_name = f"derivação 0{i}.webp"
    dst_name = f"bar-derivacao-0{i}.webp"
    src = os.path.join(DV_SRC, src_name)
    dst = os.path.join(IMG, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"  OK: {src_name} -> {dst_name}")
    else:
        print(f"  ERRO: Nao encontrou {src_name}")

print("\nTudo pronto!")

"""Troca fundo preto da imagem especial para branco"""
from PIL import Image
import numpy as np

img_path = r"C:\Users\kauap\Documents\aepaineis-site\img\din-sobmedida-especial.jpg"

img = Image.open(img_path).convert("RGB")
arr = np.array(img)

# Pixels escuros (fundo preto): R,G,B todos < 45
mask = (arr[:,:,0] < 45) & (arr[:,:,1] < 45) & (arr[:,:,2] < 45)

# Trocar para branco
arr[mask] = [255, 255, 255]

result = Image.fromarray(arr)
result.save(img_path, quality=95)
print(f"Fundo trocado para branco: {img_path}")
print("Pronto!")

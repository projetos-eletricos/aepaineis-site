"""Corrige detalhes da index.html: badge 15->20 anos, footer + Maquinas, melhora fotos maquinas"""
import os, re, glob

DIR = r"C:\Users\kauap\Documents\aepaineis-site"

# ============================================================
# 1) CORRIGIR +15 ANOS -> +20 ANOS em TODAS as paginas
# ============================================================
print("[1/3] Corrigindo '+15 anos' -> '+20 anos'...\n")

PAGES = glob.glob(os.path.join(DIR, "*.html"))
for page in PAGES:
    with open(page, 'r', encoding='utf-8') as f:
        html = f.read()
    if '+15 anos' in html:
        html = html.replace('+15 anos', '+20 anos')
        with open(page, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  {os.path.basename(page)}: +15 -> +20 anos")

# ============================================================
# 2) ADICIONAR MAQUINAS ESPECIAIS NO FOOTER
# ============================================================
print("\n[2/3] Adicionando 'Maquinas Especiais' no footer...\n")

INDEX = os.path.join(DIR, "index.html")
with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

old_footer_produtos = '''                <a href="barramento-derivacao.html">Barramento de Derivação</a>
            </div>
            <div class="footer-col">
                <h4>Contato</h4>'''

new_footer_produtos = '''                <a href="barramento-derivacao.html">Barramento de Derivação</a>
                <a href="catalogo.html#maquinas">Máquinas Especiais</a>
            </div>
            <div class="footer-col">
                <h4>Contato</h4>'''

if old_footer_produtos in html:
    html = html.replace(old_footer_produtos, new_footer_produtos)
    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(html)
    print("  index.html: Maquinas Especiais adicionado ao footer!")
else:
    if 'Máquinas Especiais' in html[html.find('footer'):] if 'footer' in html else False:
        print("  index.html: ja tem Maquinas no footer")
    else:
        print("  index.html: footer nao encontrado no formato esperado")

# Fazer o mesmo nas outras paginas
for page in PAGES:
    if os.path.basename(page) == 'index.html':
        continue
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_footer_produtos in content:
        content = content.replace(old_footer_produtos, new_footer_produtos)
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  {os.path.basename(page)}: Maquinas adicionado ao footer!")

# ============================================================
# 3) MELHORAR FOTOS DAS MAQUINAS (fundo mais limpo)
# ============================================================
print("\n[3/3] Melhorando fotos das maquinas (borda cinza -> azul)...\n")

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("  Pillow nao encontrado, instalando...")
    os.system("pip install Pillow")
    try:
        from PIL import Image
        HAS_PIL = True
    except:
        print("  ERRO: instale Pillow manualmente (pip install Pillow)")

if HAS_PIL:
    AZUL_R, AZUL_G, AZUL_B = 11, 29, 53  # #0B1D35
    IMG_DIR = os.path.join(DIR, "img")

    maquinas = [
        "home-maquina-fechamento.jpg",
        "home-maquina-tampas.jpg",
    ]

    for foto in maquinas:
        path = os.path.join(IMG_DIR, foto)
        if not os.path.exists(path):
            print(f"  {foto}: nao encontrado, pulando")
            continue

        img = Image.open(path).convert("RGBA")
        pixels = img.load()
        w, h = img.size

        # Limiar mais agressivo para pegar os cinzas claros das bordas
        LIMIAR = 50
        changed_px = 0

        for y in range(h):
            for x in range(w):
                r, g, b, a = pixels[x, y]
                # Pixels escuros (preto e cinza escuro)
                if r < LIMIAR and g < LIMIAR and b < LIMIAR:
                    pixels[x, y] = (AZUL_R, AZUL_G, AZUL_B, 255)
                    changed_px += 1
                # Pixels transparentes ou semi-transparentes
                elif a < 200:
                    pixels[x, y] = (AZUL_R, AZUL_G, AZUL_B, 255)
                    changed_px += 1

        img_rgb = img.convert("RGB")
        img_rgb.save(path, "JPEG", quality=92)
        print(f"  {foto}: {changed_px} pixels corrigidos ({w}x{h})")

print("\n" + "=" * 50)
print("  PRONTO!")
print("=" * 50)
print("\nAgora faca:")
print("  cd C:\\Users\\kauap\\Documents\\aepaineis-site")
print('  git add -A; git commit -m "Fix badge 20 anos, footer maquinas, fotos"; git push')

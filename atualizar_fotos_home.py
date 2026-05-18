"""
Copia as 10 fotos da pasta FOTOS PRIMEIRA PAGINA HOME para img/,
troca o fundo preto pelo azul padrao do site, e atualiza o carousel da index.html
e o marquee da empresa.html.
"""
import os, shutil, re

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("AVISO: Pillow nao instalado. Instalando...")
    os.system("pip install Pillow")
    try:
        from PIL import Image
        HAS_PIL = True
        print("Pillow instalado com sucesso!\n")
    except:
        print("ERRO: Nao foi possivel instalar Pillow.")
        print("Execute: pip install Pillow")
        exit(1)

# Pastas
SRC = r"C:\Users\kauap\OneDrive\Documentos\aepaineis-site\FOTOS PRIMEIRA PAGINA HOME"
DST = r"C:\Users\kauap\Documents\aepaineis-site\img"
DIR = r"C:\Users\kauap\Documents\aepaineis-site"

# Cor azul do site (RGB) - mesmo tom do hero
AZUL_R, AZUL_G, AZUL_B = 11, 29, 53  # #0B1D35

# Mapeamento: arquivo original -> nome no site
FOTOS = [
    # BARRAMENTOS
    ("kit barramento com termo 250A 60 polos.png", "home-kit-barramento-250a.png", "Kit Barramento 250A com Neutro e Terra"),
    ("barramento bifasico 1.jpeg", "home-barramento-bifasico.jpg", "Barramento Bifásico A&E Painéis"),
    ("barramento neutro 8 polos.jpeg", "home-barramento-neutro.jpg", "Barramento Neutro 8 Polos"),
    ("barramento terra 8 polos.jpeg", "home-barramento-terra.jpg", "Barramento Terra 8 Polos"),
    # QUADROS
    ("quadro de distribuição 01.png", "home-quadro-dist-01.png", "Quadro de Distribuição A&E Painéis"),
    ("quadro de distribuição 03.png", "home-quadro-dist-03.png", "Quadro de Distribuição Grande"),
    ("quadro qgbt 2.png", "home-quadro-qgbt.png", "Quadro QGBT Industrial"),
    ("sessão com varios quadros 1.png", "home-sessao-quadros.png", "Produção de Quadros em Escala"),
    # MAQUINAS
    ("máquina de fechamento superior e inferior (intermitente com visão).jpg", "home-maquina-fechamento.jpg", "Máquina de Fechamento com Visão"),
    ("máquina de montagem de tampas de 3 peças.jpg", "home-maquina-tampas.jpg", "Máquina de Montagem de Tampas"),
]

def trocar_fundo_preto_para_azul(img_path, out_path):
    """Troca pixels pretos/muito escuros pelo azul padrao do site"""
    img = Image.open(img_path).convert("RGBA")
    pixels = img.load()
    w, h = img.size

    # Limiar: pixels com R,G,B todos abaixo de 30 sao considerados "preto"
    LIMIAR = 35

    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            # Se o pixel eh muito escuro (preto ou quase preto)
            if r < LIMIAR and g < LIMIAR and b < LIMIAR:
                pixels[x, y] = (AZUL_R, AZUL_G, AZUL_B, 255)
            # Se o pixel eh transparente, colocar azul
            elif a < 128:
                pixels[x, y] = (AZUL_R, AZUL_G, AZUL_B, 255)

    # Salvar como RGB (sem transparencia)
    img_rgb = img.convert("RGB")

    # Determinar formato de saida
    if out_path.lower().endswith('.png'):
        img_rgb.save(out_path, "PNG", optimize=True)
    else:
        img_rgb.save(out_path, "JPEG", quality=92)

    return img.size

print("=" * 60)
print("  ATUALIZANDO FOTOS DA HOME - A&E Painéis")
print("=" * 60)

# 1) Processar e copiar fotos
print("\n[1/3] Processando fotos (preto -> azul)...\n")
for original, destino, alt in FOTOS:
    src_path = os.path.join(SRC, original)
    dst_path = os.path.join(DST, destino)

    if not os.path.exists(src_path):
        print(f"  ERRO: {original} nao encontrado!")
        continue

    size = trocar_fundo_preto_para_azul(src_path, dst_path)
    print(f"  OK: {original}")
    print(f"      -> {destino} ({size[0]}x{size[1]})")

# 2) Atualizar index.html - Hero Carousel
print("\n[2/3] Atualizando carousel da index.html...\n")

INDEX = os.path.join(DIR, "index.html")
with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

# Novo carousel com as 10 fotos na ordem: barramentos > quadros > maquinas
new_imgs = ""
for i, (original, destino, alt) in enumerate(FOTOS):
    active = ' class="active"' if i == 0 else ''
    new_imgs += f'                    <img src="img/{destino}" alt="{alt}"{active}>\n'

# Substituir conteudo do carousel
pattern = r'(<div class="hero-carousel" id="heroCarousel">)\s*\n(.*?)(                    <div class="hero-carousel-dots")'
match = re.search(pattern, html, re.DOTALL)
if match:
    html = html[:match.end(1)] + '\n' + new_imgs + match.group(3) + html[match.end(3):]
    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(html)
    print("  Carousel atualizado com 10 fotos!")
    print("  Barramentos (4): kit-250a, bifasico, neutro, terra")
    print("  Quadros (4): dist-01, dist-03, qgbt, sessao")
    print("  Maquinas (2): fechamento, tampas")
else:
    print("  ERRO: Carousel nao encontrado!")

# 3) Atualizar empresa.html - Marquee
print("\n[3/3] Atualizando marquee da empresa.html...\n")

EMPRESA = os.path.join(DIR, "empresa.html")
with open(EMPRESA, 'r', encoding='utf-8') as f:
    html_emp = f.read()

# Gerar sequencia de imagens para o marquee
marquee_imgs = '        <!-- Sequência 1: Barramentos > Quadros > Máquinas -->\n'
for original, destino, alt in FOTOS:
    marquee_imgs += f'        <img src="img/{destino}" alt="{alt}">\n'
marquee_imgs += '        <!-- Duplicado para loop contínuo -->\n'
for original, destino, alt in FOTOS:
    marquee_imgs += f'        <img src="img/{destino}" alt="{alt}">\n'

marquee_pattern = r'(<div class="hero-marquee">)\s*\n(.*?)\n(\s*</div>\s*\n\s*</section>)'
match = re.search(marquee_pattern, html_emp, re.DOTALL)
if match:
    new_html = html_emp[:match.end(1)] + '\n' + marquee_imgs + '    ' + html_emp[match.start(3):]
    with open(EMPRESA, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("  Marquee atualizado com 10 fotos (x2 para loop)!")
else:
    print("  ERRO: Marquee nao encontrado!")

print("\n" + "=" * 60)
print("  PRONTO! Fotos processadas e HTML atualizado.")
print("=" * 60)
print("\nAgora faca:")
print("  cd C:\\Users\\kauap\\Documents\\aepaineis-site")
print("  git add -A; git commit -m 'Fotos novas home com fundo azul'; git push")

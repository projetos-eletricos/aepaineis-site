"""Aplica o fundo azul CTA nas secoes 'Quem Somos' e 'Numeros' da pagina Empresa"""
import re, os

FILE = os.path.join(r"C:\Users\kauap\Documents\aepaineis-site", "empresa.html")

with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

changed = False

# ============================================================
# 1) TROCAR FUNDO DO HERO (empresa-hero) PARA O ESTILO CTA
# ============================================================
CTA_BG = "linear-gradient(135deg, #040d1a 0%, #0a1929 20%, #0f2744 45%, #122d4f 60%, #0a1f3a 80%, #060e1e 100%)"
CTA_PATTERN = """background-image:
                linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
            background-size:60px 60px;"""

# Hero: trocar o background
old_hero_bg = "background: var(--gradient-hero);"
# Encontrar dentro do .empresa-hero
if '.empresa-hero {' in html:
    # Trocar o background do empresa-hero
    hero_pattern = r'(\.empresa-hero\s*\{[^}]*?)background:\s*var\(--gradient-hero\);'
    hero_replacement = r'\1background: ' + CTA_BG + ';'
    new_html = re.sub(hero_pattern, hero_replacement, html)
    if new_html != html:
        html = new_html
        changed = True
        print("  [HERO] Fundo trocado para CTA gradient!")

    # Trocar o ::before pattern do hero para o grid CTA
    old_hero_before_pattern = r"(\.empresa-hero::before\s*\{[^}]*?)background:\s*url\([^)]+\);"
    new_hero_before = r"\1" + CTA_PATTERN
    new_html = re.sub(old_hero_before_pattern, new_hero_before, html)
    if new_html != html:
        html = new_html
        changed = True
        print("  [HERO] Pattern trocado para grid CTA!")

# ============================================================
# 2) TROCAR FUNDO DOS NUMEROS PARA O ESTILO CTA
# ============================================================
if '.numbers-section {' in html:
    num_pattern = r'(\.numbers-section\s*\{[^}]*?)background:\s*var\(--gradient-hero\);'
    num_replacement = r'\1background: ' + CTA_BG + ';'
    new_html = re.sub(num_pattern, num_replacement, html)
    if new_html != html:
        html = new_html
        changed = True
        print("  [NUMEROS] Fundo trocado para CTA gradient!")

    # Trocar o ::before pattern dos numeros para o grid CTA
    old_num_before = r"(\.numbers-section::before\s*\{[^}]*?)background:\s*url\([^)]+\);"
    new_num_before = r"\1" + CTA_PATTERN
    new_html = re.sub(old_num_before, new_num_before, html)
    if new_html != html:
        html = new_html
        changed = True
        print("  [NUMEROS] Pattern trocado para grid CTA!")

# ============================================================
# 3) ATUALIZAR NUMEROS (caso nao tenha sido feito ainda)
# ============================================================
if 'data-count="500"' in html:
    html = html.replace('data-count="500"', 'data-count="3000"')
    changed = True
    print("  [NUMEROS] 500 -> 3000 Projetos")

if '<div class="number-value" data-count="15">' in html:
    html = html.replace(
        '<div class="number-value" data-count="15">',
        '<div class="number-value" data-count="20">'
    )
    changed = True
    print("  [NUMEROS] 15 -> 20 Anos")

if 'data-count="200"' in html:
    html = html.replace('data-count="200"', 'data-count="1000"')
    changed = True
    print("  [NUMEROS] 200 -> 1000 Clientes")

if 'data-count="100"' in html:
    html = html.replace('data-count="100"', 'data-count="0"')
    html = html.replace('Satisfação Garantida', 'Devoluções')
    changed = True
    print("  [NUMEROS] 100% Satisfacao -> 0 Devolucoes")

# Story accent box 15 -> 20
if '<div class="sab-number" data-count="15">' in html:
    html = html.replace(
        '<div class="sab-number" data-count="15">',
        '<div class="sab-number" data-count="20">'
    )
    changed = True
    print("  [STORY] 15 -> 20 Anos de Mercado")

# Fix counter JS para valor 0
if "t+(t===100?'%':'+')" in html and "t===0" not in html:
    html = html.replace(
        "t+(t===100?'%':'+')",
        "t+(t===0?'':t===100?'%':'+')"
    )
    changed = True
    print("  [JS] Fix contador para valor 0")

if changed:
    with open(FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    print("\n  empresa.html SALVO!")
else:
    print("\n  Nenhuma alteracao necessaria")

print("\nPronto!")

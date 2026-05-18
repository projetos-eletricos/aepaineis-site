"""Troca fotos do carousel da index.html por fotos melhores (mais claras e com qualidade)
Ordem: Barramentos > Quadros > Maquinas"""
import os

DIR = r"C:\Users\kauap\Documents\aepaineis-site"

# ============================================================
# INDEX.HTML - Hero Carousel
# ============================================================
INDEX = os.path.join(DIR, "index.html")

with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

# Fotos atuais (escuras / sem qualidade)
old_carousel = '''                    <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico com Neutro e Terra A&E Painéis" class="active">
                    <img src="img/home-sessao-quadros.jpg" alt="Produção de Quadros Elétricos em Escala">
                    <img src="img/home-qgbt-2.jpg" alt="Quadro QGBT A&E Painéis">
                    <img src="img/home-quadro-dist-01.jpg" alt="Quadro de Distribuição Completo">
                    <img src="img/home-maquina-tampas.jpg" alt="Máquina Especial de Montagem">'''

# Novas fotos: melhores, mais claras, na ordem certa
new_carousel = '''                    <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico com Neutro e Terra A&E Painéis" class="active">
                    <img src="img/quadro-distribuicao-1.jpg" alt="Quadro de Distribuição A&E Painéis">
                    <img src="img/quadro-distribuicao-2.jpg" alt="Quadro QGBT Industrial A&E Painéis">
                    <img src="img/maquina-fechamento-visao.jpg" alt="Máquina de Fechamento por Visão A&E Painéis">
                    <img src="img/maquina-montagem-tampas-3-pecas.jpg" alt="Máquina de Montagem de Tampas A&E Painéis">'''

changed = False

if old_carousel in html:
    html = html.replace(old_carousel, new_carousel)
    changed = True
    print("[INDEX] Carousel atualizado com fotos melhores!")
    print("  1. home-kit-trifasico.jpg (barramento - mantida)")
    print("  2. quadro-distribuicao-1.jpg (quadro - overhead, vibrante)")
    print("  3. quadro-distribuicao-2.jpg (QGBT grande, real)")
    print("  4. maquina-fechamento-visao.jpg (fundo branco, profissional)")
    print("  5. maquina-montagem-tampas-3-pecas.jpg (fundo branco, profissional)")
else:
    # Tentar a ordem que o script anterior pode ter colocado
    old_carousel_v2 = '''                    <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico com Neutro e Terra A&E Painéis" class="active">
                    <img src="img/home-sessao-quadros.jpg" alt="Produção de Quadros Elétricos em Escala">
                    <img src="img/home-qgbt-2.jpg" alt="Quadro QGBT A&E Painéis">
                    <img src="img/home-maquina-tampas.jpg" alt="Máquina Especial de Montagem">
                    <img src="img/home-quadro-dist-01.jpg" alt="Quadro de Distribuição Completo">'''
    if old_carousel_v2 in html:
        html = html.replace(old_carousel_v2, new_carousel)
        changed = True
        print("[INDEX] Carousel atualizado (v2) com fotos melhores!")
    else:
        print("[INDEX] AVISO: Carousel nao encontrado na ordem esperada")
        print("  Buscando padrao alternativo...")
        # Buscar por qualquer combinacao que tenha as 5 fotos antigas
        import re
        pattern = r'(<div class="hero-carousel" id="heroCarousel">)\s*\n(.*?)(                    <div class="hero-carousel-dots")'
        match = re.search(pattern, html, re.DOTALL)
        if match:
            new_imgs = '''
                    <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico com Neutro e Terra A&E Painéis" class="active">
                    <img src="img/quadro-distribuicao-1.jpg" alt="Quadro de Distribuição A&E Painéis">
                    <img src="img/quadro-distribuicao-2.jpg" alt="Quadro QGBT Industrial A&E Painéis">
                    <img src="img/maquina-fechamento-visao.jpg" alt="Máquina de Fechamento por Visão A&E Painéis">
                    <img src="img/maquina-montagem-tampas-3-pecas.jpg" alt="Máquina de Montagem de Tampas A&E Painéis">
'''
            html = html[:match.start(2)] + new_imgs + html[match.start(3):]
            changed = True
            print("[INDEX] Carousel atualizado via regex!")
        else:
            print("[INDEX] ERRO: Nao consegui encontrar o carousel")

if changed:
    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(html)
    print("\n  index.html SALVO!")

# ============================================================
# EMPRESA.HTML - Marquee (atualizar tambem)
# ============================================================
EMPRESA = os.path.join(DIR, "empresa.html")

with open(EMPRESA, 'r', encoding='utf-8') as f:
    html_emp = f.read()

# Fotos organizadas do script anterior (ou original)
# Vamos trocar TODAS as fotos ruins por melhores, mantendo ordem: barramento > quadro > maquina

# Nova sequencia organizada com as MELHORES fotos
new_marquee_imgs = '''        <!-- Sequência 1: Barramentos > Quadros > Máquinas -->
        <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico">
        <img src="img/home-kit-250a.jpg" alt="Kit Barramento 250A">
        <img src="img/home-barra-bifasico.jpg" alt="Barramento Bifásico">
        <img src="img/home-barra-neutro.jpg" alt="Barramento Neutro">
        <img src="img/home-barra-terra.jpg" alt="Barramento Terra">
        <img src="img/quadro-distribuicao-1.jpg" alt="Quadro de Distribuição">
        <img src="img/quadro-distribuicao-2.jpg" alt="Quadro QGBT Industrial">
        <img src="img/sessao-quadros-2.jpg" alt="Quadros em Produção">
        <img src="img/sessao-quadros-7.jpg" alt="Produção de Quadros em Escala">
        <img src="img/maquina-fechamento-visao.jpg" alt="Máquina de Fechamento por Visão">
        <img src="img/maquina-montagem-tampas-3-pecas.jpg" alt="Máquina de Montagem de Tampas">
        <img src="img/maquina-frascos-infusao.jpg" alt="Máquina de Frascos de Infusão">
        <!-- Duplicado para loop contínuo -->
        <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico">
        <img src="img/home-kit-250a.jpg" alt="Kit Barramento 250A">
        <img src="img/home-barra-bifasico.jpg" alt="Barramento Bifásico">
        <img src="img/home-barra-neutro.jpg" alt="Barramento Neutro">
        <img src="img/home-barra-terra.jpg" alt="Barramento Terra">
        <img src="img/quadro-distribuicao-1.jpg" alt="Quadro de Distribuição">
        <img src="img/quadro-distribuicao-2.jpg" alt="Quadro QGBT Industrial">
        <img src="img/sessao-quadros-2.jpg" alt="Quadros em Produção">
        <img src="img/sessao-quadros-7.jpg" alt="Produção de Quadros em Escala">
        <img src="img/maquina-fechamento-visao.jpg" alt="Máquina de Fechamento por Visão">
        <img src="img/maquina-montagem-tampas-3-pecas.jpg" alt="Máquina de Montagem de Tampas">
        <img src="img/maquina-frascos-infusao.jpg" alt="Máquina de Frascos de Infusão">'''

import re

# Encontrar o conteudo do marquee entre <div class="hero-marquee"> e </div>
marquee_pattern = r'(<div class="hero-marquee">)\s*\n(.*?)\n(\s*</div>\s*\n\s*</section>)'
match = re.search(marquee_pattern, html_emp, re.DOTALL)

if match:
    new_html_emp = html_emp[:match.end(1)] + '\n' + new_marquee_imgs + '\n    ' + html_emp[match.start(3):]
    with open(EMPRESA, 'w', encoding='utf-8') as f:
        f.write(new_html_emp)
    print("\n[EMPRESA] Marquee atualizado com fotos melhores!")
    print("  Barramentos (5): kit-trifasico, kit-250a, bifasico, neutro, terra")
    print("  Quadros (4): distribuicao-1, distribuicao-2, sessao-2, sessao-7")
    print("  Maquinas (3): fechamento-visao, montagem-tampas, frascos-infusao")
else:
    print("\n[EMPRESA] AVISO: Marquee nao encontrado via regex")

print("\nPronto! Agora faca:")
print("  cd C:\\Users\\kauap\\Documents\\aepaineis-site")
print("  git add -A; git commit -m 'Fotos melhores no carousel e marquee'; git push")

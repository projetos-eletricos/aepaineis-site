"""Reorganiza fotos: Barramentos -> Quadros -> Maquinas (index.html e empresa.html)"""
import os

DIR = r"C:\Users\kauap\Documents\aepaineis-site"

# ============================================================
# 1) INDEX.HTML - Hero Carousel (5 fotos)
# ============================================================
INDEX = os.path.join(DIR, "index.html")

with open(INDEX, 'r', encoding='utf-8') as f:
    html_index = f.read()

# Ordem atual no carousel:
old_carousel = '''                    <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico com Neutro e Terra A&E Painéis" class="active">
                    <img src="img/home-sessao-quadros.jpg" alt="Produção de Quadros Elétricos em Escala">
                    <img src="img/home-qgbt-2.jpg" alt="Quadro QGBT A&E Painéis">
                    <img src="img/home-maquina-tampas.jpg" alt="Máquina Especial de Montagem">
                    <img src="img/home-quadro-dist-01.jpg" alt="Quadro de Distribuição Completo">'''

# Nova ordem: Barramento -> Quadros -> Maquina
new_carousel = '''                    <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico com Neutro e Terra A&E Painéis" class="active">
                    <img src="img/home-sessao-quadros.jpg" alt="Produção de Quadros Elétricos em Escala">
                    <img src="img/home-qgbt-2.jpg" alt="Quadro QGBT A&E Painéis">
                    <img src="img/home-quadro-dist-01.jpg" alt="Quadro de Distribuição Completo">
                    <img src="img/home-maquina-tampas.jpg" alt="Máquina Especial de Montagem">'''

if old_carousel in html_index:
    html_index = html_index.replace(old_carousel, new_carousel)
    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(html_index)
    print("[INDEX] Carousel reorganizado: Barramento > Quadros > Maquina")
else:
    print("[INDEX] Carousel ja esta na ordem correta ou nao encontrado")

# ============================================================
# 2) EMPRESA.HTML - Marquee (13 fotos, duplicadas para loop)
# ============================================================
EMPRESA = os.path.join(DIR, "empresa.html")

with open(EMPRESA, 'r', encoding='utf-8') as f:
    html_empresa = f.read()

# Ordem atual (misturada):
old_seq1 = '''        <!-- Sequência 1 -->
        <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico">
        <img src="img/home-quadro-dist-01.jpg" alt="Quadro de Distribuição">
        <img src="img/home-maquina-tampas.jpg" alt="Máquina de Montagem">
        <img src="img/home-qgbt-2.jpg" alt="Quadro QGBT">
        <img src="img/home-kit-250a.jpg" alt="Kit Barramento 250A">
        <img src="img/home-sessao-quadros.jpg" alt="Produção em Escala">
        <img src="img/home-barra-bifasico.jpg" alt="Barramento Bifásico">
        <img src="img/home-quadro-dist-02.jpg" alt="Quadro de Distribuição">
        <img src="img/home-maquina-fechamento.jpg" alt="Máquina de Fechamento">
        <img src="img/home-qgbt-1.jpg" alt="Quadro QGBT Grande">
        <img src="img/home-barra-neutro.jpg" alt="Barramento Neutro">
        <img src="img/home-quadro-dist-03.jpg" alt="Quadro de Distribuição">
        <img src="img/home-barra-terra.jpg" alt="Barramento Terra">
        <!-- Duplicado para loop contínuo -->
        <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico">
        <img src="img/home-quadro-dist-01.jpg" alt="Quadro de Distribuição">
        <img src="img/home-maquina-tampas.jpg" alt="Máquina de Montagem">
        <img src="img/home-qgbt-2.jpg" alt="Quadro QGBT">
        <img src="img/home-kit-250a.jpg" alt="Kit Barramento 250A">
        <img src="img/home-sessao-quadros.jpg" alt="Produção em Escala">
        <img src="img/home-barra-bifasico.jpg" alt="Barramento Bifásico">
        <img src="img/home-quadro-dist-02.jpg" alt="Quadro de Distribuição">
        <img src="img/home-maquina-fechamento.jpg" alt="Máquina de Fechamento">
        <img src="img/home-qgbt-1.jpg" alt="Quadro QGBT Grande">
        <img src="img/home-barra-neutro.jpg" alt="Barramento Neutro">
        <img src="img/home-quadro-dist-03.jpg" alt="Quadro de Distribuição">
        <img src="img/home-barra-terra.jpg" alt="Barramento Terra">'''

# Nova ordem: BARRAMENTOS (5) -> QUADROS (6) -> MAQUINAS (2)
new_seq1 = '''        <!-- Sequência 1: Barramentos > Quadros > Máquinas -->
        <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico">
        <img src="img/home-kit-250a.jpg" alt="Kit Barramento 250A">
        <img src="img/home-barra-bifasico.jpg" alt="Barramento Bifásico">
        <img src="img/home-barra-neutro.jpg" alt="Barramento Neutro">
        <img src="img/home-barra-terra.jpg" alt="Barramento Terra">
        <img src="img/home-sessao-quadros.jpg" alt="Produção em Escala">
        <img src="img/home-quadro-dist-01.jpg" alt="Quadro de Distribuição">
        <img src="img/home-quadro-dist-02.jpg" alt="Quadro de Distribuição">
        <img src="img/home-quadro-dist-03.jpg" alt="Quadro de Distribuição">
        <img src="img/home-qgbt-1.jpg" alt="Quadro QGBT Grande">
        <img src="img/home-qgbt-2.jpg" alt="Quadro QGBT">
        <img src="img/home-maquina-tampas.jpg" alt="Máquina de Montagem">
        <img src="img/home-maquina-fechamento.jpg" alt="Máquina de Fechamento">
        <!-- Duplicado para loop contínuo -->
        <img src="img/home-kit-trifasico.jpg" alt="Kit Barramento Trifásico">
        <img src="img/home-kit-250a.jpg" alt="Kit Barramento 250A">
        <img src="img/home-barra-bifasico.jpg" alt="Barramento Bifásico">
        <img src="img/home-barra-neutro.jpg" alt="Barramento Neutro">
        <img src="img/home-barra-terra.jpg" alt="Barramento Terra">
        <img src="img/home-sessao-quadros.jpg" alt="Produção em Escala">
        <img src="img/home-quadro-dist-01.jpg" alt="Quadro de Distribuição">
        <img src="img/home-quadro-dist-02.jpg" alt="Quadro de Distribuição">
        <img src="img/home-quadro-dist-03.jpg" alt="Quadro de Distribuição">
        <img src="img/home-qgbt-1.jpg" alt="Quadro QGBT Grande">
        <img src="img/home-qgbt-2.jpg" alt="Quadro QGBT">
        <img src="img/home-maquina-tampas.jpg" alt="Máquina de Montagem">
        <img src="img/home-maquina-fechamento.jpg" alt="Máquina de Fechamento">'''

if old_seq1 in html_empresa:
    html_empresa = html_empresa.replace(old_seq1, new_seq1)
    with open(EMPRESA, 'w', encoding='utf-8') as f:
        f.write(html_empresa)
    print("[EMPRESA] Marquee reorganizado: 5 Barramentos > 6 Quadros > 2 Maquinas")
else:
    print("[EMPRESA] Marquee nao encontrado na ordem esperada")
    # Tentar verificar se ja esta organizado
    if 'Barramentos > Quadros' in html_empresa:
        print("  -> Ja esta organizado!")
    else:
        print("  -> ERRO: verificar manualmente")

print("\nPronto! Agora faca:")
print("  cd C:\\Users\\kauap\\Documents\\aepaineis-site")
print('  git add -A && git commit -m "Fotos organizadas: barramentos > quadros > maquinas" && git push')

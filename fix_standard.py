"""Aplica todas as alteracoes da Linha Standard"""
import os

FILE = r"C:\Users\kauap\Documents\aepaineis-site\barramento-padrao-din.html"

with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# Verificar se ja tem os cards novos
if 'std-grid' in html:
    print("Cards novos ja presentes, verificando fotos...")
    # Inverter fotos bifasico: 1 vira principal -> 2 vira principal
    if 'standard-bifasico-1.png" alt="Barramento Bifásico Standard" id="bifImg"' in html:
        html = html.replace(
            'standard-bifasico-1.png" alt="Barramento Bifásico Standard" id="bifImg"',
            'standard-bifasico-2.png" alt="Barramento Bifásico Standard" id="bifImg"'
        )
        html = html.replace(
            'standard-bifasico-1.png" alt="Bifásico 1"',
            'standard-bifasico-2.png" alt="Bifásico 1"'
        )
        html = html.replace(
            'standard-bifasico-2.png" alt="Bifásico 2"',
            'standard-bifasico-1.png" alt="Bifásico 2"'
        )
        print("Fotos bifasico invertidas!")
    else:
        print("Fotos ja estao invertidas.")

    with open(FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Arquivo salvo!")
else:
    print("AVISO: Os cards novos NAO estao no arquivo.")
    print("Verifique se o arquivo foi atualizado corretamente.")

print("\nVerificando submenu nas outras paginas...")

# Remover submenu dropdown-has-sub em todas as paginas
PAGES = [
    'index.html', 'barramento-padrao-din.html', 'barramento-especial-din.html',
    'barramento-neutro-terra.html', 'barramento-derivacao.html', 'catalogo.html',
    'empresa.html', 'contato.html', 'barramentos-especiais.html'
]

old_submenu = '''                    <div class="dropdown-has-sub">
                        <a href="barramento-padrao-din.html"><svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>Linha DIN Standard</a>
                        <div class="dropdown-submenu">'''

new_link = '                    <a href="barramento-padrao-din.html"><svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>Linha DIN Standard</a>'

DIR = r"C:\Users\kauap\Documents\aepaineis-site"

for page in PAGES:
    path = os.path.join(DIR, page)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'dropdown-has-sub' in content:
        # Remove the entire dropdown-has-sub block
        import re
        pattern = r'<div class="dropdown-has-sub">\s*<a href="barramento-padrao-din\.html">.*?Linha DIN Standard</a>\s*<div class="dropdown-submenu">.*?</div>\s*</div>'
        replacement = new_link
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  {page}: submenu removido!")
        else:
            print(f"  {page}: nenhuma alteracao")
    else:
        print(f"  {page}: ja esta sem submenu")

print("\nPronto! Agora faca: git add -A && git commit -m 'Linha Standard atualizada' && git push")

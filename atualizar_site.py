"""
Script completo de atualizacoes pendentes:
1. Linha Standard: novos cards bifasico/trifasico + fotos + form com amperagem
2. Remove submenu dropdown da Linha Standard em TODAS as paginas
3. Empresa: atualiza numeros (3000+, 20+, 1000+, 0 Devolucoes)
"""
import os, re

DIR = r"C:\Users\kauap\Documents\aepaineis-site"

def read_file(name):
    path = os.path.join(DIR, name)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(name, content):
    path = os.path.join(DIR, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# ============================================================
# 1) REMOVER SUBMENU DA LINHA STANDARD EM TODAS AS PAGINAS
# ============================================================
PAGES = [
    'index.html', 'barramento-padrao-din.html', 'barramento-especial-din.html',
    'barramento-neutro-terra.html', 'barramento-derivacao.html', 'catalogo.html',
    'empresa.html', 'contato.html', 'barramentos-especiais.html'
]

new_link = '                    <a href="barramento-padrao-din.html"><svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>Linha DIN Standard</a>'

for page in PAGES:
    path = os.path.join(DIR, page)
    if not os.path.exists(path):
        continue
    content = read_file(page)
    if 'dropdown-has-sub' in content:
        pattern = r'<div class="dropdown-has-sub">\s*<a href="barramento-padrao-din\.html">.*?Linha DIN Standard</a>\s*<div class="dropdown-submenu">.*?</div>\s*</div>'
        new_content = re.sub(pattern, new_link, content, flags=re.DOTALL)
        if new_content != content:
            write_file(page, new_content)
            print(f"  [SUBMENU] {page}: removido!")
        else:
            print(f"  [SUBMENU] {page}: sem alteracao")
    else:
        print(f"  [SUBMENU] {page}: ja sem submenu")

# ============================================================
# 2) ATUALIZAR PAGINA LINHA STANDARD (barramento-padrao-din.html)
# ============================================================
print("\n--- LINHA STANDARD ---")
std = read_file('barramento-padrao-din.html')

# Verificar se ja tem os cards novos
if 'std-grid' not in std:
    # Substituir toda a secao de produto antiga pelos novos cards
    old_section_pattern = r'<!-- PRODUCT CONTENT -->.*?</section>'

    new_section = '''<!-- PRODUCT CARDS -->
<section class="section">
    <div class="wrap">
        <style>
            .std-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:32px;margin-bottom:48px}
            .std-card{background:#fff;border-radius:var(--radius);border:1px solid var(--border);overflow:hidden;transition:box-shadow .3s,border-color .3s}
            .std-card:hover{border-color:var(--accent);box-shadow:var(--shadow)}
            .std-card-img{width:100%;background:#fff;display:flex;align-items:center;justify-content:center;padding:20px;border-bottom:1px solid var(--border)}
            .std-card-img img{width:100%;height:auto;object-fit:contain;max-height:320px}
            .std-card-body{padding:28px}
            .std-card-badge{display:inline-block;background:var(--primary);color:#fff;font-size:11px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;padding:4px 12px;border-radius:20px;margin-bottom:14px}
            .std-card-body h3{font-family:var(--font-display);font-size:20px;font-weight:700;color:var(--primary);margin-bottom:10px}
            .std-card-body p{font-size:14.5px;color:var(--text-secondary);line-height:1.7;margin-bottom:18px}
            .std-card-specs{display:flex;flex-direction:column;gap:8px;margin-bottom:20px}
            .std-card-specs span{display:flex;align-items:center;gap:8px;font-size:13.5px;color:var(--text-secondary)}
            .std-card-specs span svg{width:16px;height:16px;stroke:var(--accent);stroke-width:2.5;fill:none;flex-shrink:0}
            .std-card-gallery{display:flex;gap:8px;padding:0 28px 20px}
            .std-card-gallery img{width:72px;height:72px;object-fit:cover;border-radius:8px;border:1px solid var(--border);cursor:pointer;transition:border-color .2s}
            .std-card-gallery img:hover{border-color:var(--accent)}
            .std-quote{background:#fff;border-radius:var(--radius);border:1px solid var(--border);padding:36px;box-shadow:var(--shadow)}
            .std-quote h3{font-family:var(--font-display);font-size:22px;font-weight:700;color:var(--primary);margin-bottom:6px}
            .std-quote>p{font-size:14px;color:var(--text-secondary);margin-bottom:24px}
            .std-quote .qf-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
            .std-quote label{font-size:13px;font-weight:600;color:var(--text-secondary);margin-bottom:6px;display:block}
            .std-quote input,.std-quote select,.std-quote textarea{width:100%;padding:10px 14px;border:1px solid var(--border);border-radius:8px;font-size:14px;font-family:var(--font-body);transition:border-color .2s}
            .std-quote input:focus,.std-quote select:focus,.std-quote textarea:focus{outline:none;border-color:var(--accent)}
            .std-quote textarea{resize:vertical;min-height:80px}
            @media(max-width:600px){.std-grid{grid-template-columns:1fr}.std-quote .qf-grid{grid-template-columns:1fr}}
        </style>

        <!-- Product Cards -->
        <div class="std-grid">
            <!-- BIFASICO -->
            <div class="std-card reveal" id="bifasico">
                <div class="std-card-img">
                    <img src="img/standard-bifasico-2.png" alt="Barramento Bifasico Standard" id="bifImg">
                </div>
                <div class="std-card-gallery">
                    <img src="img/standard-bifasico-2.png" alt="Bifasico 1" onclick="document.getElementById('bifImg').src=this.src">
                    <img src="img/standard-bifasico-1.png" alt="Bifasico 2" onclick="document.getElementById('bifImg').src=this.src">
                </div>
                <div class="std-card-body">
                    <span class="std-card-badge">Bifasico</span>
                    <h3>Barramento Bifasico Standard</h3>
                    <p>Barramento bifasico em cobre eletrolitico de alta pureza com banho de nitrato de prata. Disponivel de 100A a 225A, conforme a necessidade do seu projeto.</p>
                    <div class="std-card-specs">
                        <span><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Corrente nominal: 100A a 225A</span>
                        <span><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Configuracao: Bifasico</span>
                        <span><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Cobre eletrolitico com banho de prata</span>
                        <span><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Fornecido com isoladores e trilhos DIN</span>
                        <span><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Derivacao 40A inclusa</span>
                    </div>
                </div>
            </div>

            <!-- TRIFASICO -->
            <div class="std-card reveal reveal-d2" id="trifasico">
                <div class="std-card-img">
                    <img src="img/standard-trifasico-1.png" alt="Barramento Trifasico Standard" id="triImg">
                </div>
                <div class="std-card-gallery">
                    <img src="img/standard-trifasico-1.png" alt="Trifasico 1" onclick="document.getElementById('triImg').src=this.src">
                    <img src="img/standard-trifasico-2.png" alt="Trifasico 2" onclick="document.getElementById('triImg').src=this.src">
                </div>
                <div class="std-card-body">
                    <span class="std-card-badge">Trifasico</span>
                    <h3>Barramento Trifasico Standard</h3>
                    <p>Barramento trifasico em cobre eletrolitico de alta pureza. Disponivel de 100A a 225A, ideal para quadros de distribuicao trifasicos industriais e comerciais.</p>
                    <div class="std-card-specs">
                        <span><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Corrente nominal: 100A a 225A</span>
                        <span><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Configuracao: Trifasico</span>
                        <span><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Cobre eletrolitico com banho de prata</span>
                        <span><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Fornecido com isoladores e trilhos DIN</span>
                        <span><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Derivacao 40A inclusa</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Quote Form -->
        <div class="std-quote reveal" id="orcamento">
            <h3>Faca seu Orcamento</h3>
            <p>Selecione o produto, a amperagem desejada e envie seu pedido diretamente pelo WhatsApp.</p>
            <form id="quoteForm">
                <div class="qf-grid">
                    <input type="text" placeholder="CNPJ / CPF *" id="qCnpj" required>
                    <input type="text" placeholder="Seu nome *" id="qNome" required>
                </div>
                <div class="qf-grid" style="margin-top:14px">
                    <div>
                        <label>Produto *</label>
                        <select id="qProduto">
                            <option>Barramento Bifasico</option>
                            <option>Barramento Trifasico</option>
                        </select>
                    </div>
                    <div>
                        <label>Amperagem *</label>
                        <select id="qAmperagem">
                            <option>100A</option>
                            <option>150A</option>
                            <option>225A</option>
                        </select>
                    </div>
                </div>
                <div class="qf-grid" style="margin-top:14px">
                    <div>
                        <label>Cobre Eletrolitico *</label>
                        <select id="qCobre">
                            <option>Com banho de prata</option>
                            <option>Sem banho (cobre nu)</option>
                        </select>
                    </div>
                    <div>
                        <label>Quantidade de Polos *</label>
                        <select id="qPolos">''' + ''.join([f'\n                            <option>{i} Polos</option>' for i in range(12, 122, 2)]) + '''
                        </select>
                    </div>
                </div>
                <div class="qf-grid" style="margin-top:14px">
                    <input type="number" placeholder="Quantidade de pecas *" id="qQtd" min="1" required>
                    <div>
                        <label>Vai precisar de Terra?</label>
                        <div style="display:flex;gap:8px;align-items:center">
                            <select id="qTerra" onchange="document.getElementById('terraFuros').style.display=this.selectedIndex===1?'block':'none'" style="flex:1">
                                <option>Nao</option>
                                <option>Sim</option>
                            </select>
                            <input type="number" id="terraFuros" placeholder="Qtd. furos" min="1" style="display:none;width:100px;flex-shrink:0">
                        </div>
                    </div>
                </div>
                <div class="qf-grid" style="margin-top:14px">
                    <div>
                        <label>Vai precisar de Neutro?</label>
                        <div style="display:flex;gap:8px;align-items:center">
                            <select id="qNeutro" onchange="document.getElementById('neutroFuros').style.display=this.selectedIndex===1?'block':'none'" style="flex:1">
                                <option>Nao</option>
                                <option>Sim</option>
                            </select>
                            <input type="number" id="neutroFuros" placeholder="Qtd. furos" min="1" style="display:none;width:100px;flex-shrink:0">
                        </div>
                    </div>
                </div>
                <textarea placeholder="Adicione sua observacao..." id="qObs" style="margin-top:14px;width:100%"></textarea>
                <div style="margin-top:18px;text-align:center">
                    <button type="submit" class="btn-primary" style="width:100%;max-width:400px;margin:0 auto">
                        <svg viewBox="0 0 24 24" fill="currentColor" style="width:16px;height:16px"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 2C6.477 2 2 6.477 2 12c0 1.89.525 3.66 1.438 5.168L2 22l4.832-1.438A9.955 9.955 0 0012 22c5.523 0 10-4.477 10-10S17.523 2 12 2zm0 18a8 8 0 01-4.243-1.214l-.252-.149-2.868.852.852-2.868-.168-.268A8 8 0 1112 20z"/></svg>
                        Orcar pelo WhatsApp
                    </button>
                </div>
            </form>
        </div>
    </div>
</section>'''

    new_std = re.sub(old_section_pattern, new_section, std, flags=re.DOTALL)

    # Also update the JS section
    old_js = r"// Auto-select product from URL hash.*?function changeImg\(thumb, src\) \{.*?\}"
    new_js = """// Auto-select product from URL hash
(function(){
    const hash = window.location.hash.replace('#','');
    const sel = document.getElementById('qProduto');
    if(hash === 'trifasico') sel.value = 'Barramento Trifasico';
    if(hash){
        const el = document.getElementById(hash);
        if(el) setTimeout(()=>el.scrollIntoView({behavior:'smooth',block:'start'}),300);
    }
})();

document.getElementById('quoteForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const terraVal = document.getElementById('qTerra').value;
    const neutroVal = document.getElementById('qNeutro').value;
    const terraFuros = document.getElementById('terraFuros').value;
    const neutroFuros = document.getElementById('neutroFuros').value;
    const terraText = terraVal === 'Sim' ? 'Sim — ' + (terraFuros || '?') + ' furos' : 'Nao';
    const neutroText = neutroVal === 'Sim' ? 'Sim — ' + (neutroFuros || '?') + ' furos' : 'Nao';
    const msg = encodeURIComponent(
        'Ola! Gostaria de um orcamento.\\n\\nProduto: ' + document.getElementById('qProduto').value +
        '\\nAmperagem: ' + document.getElementById('qAmperagem').value +
        '\\nCobre: ' + document.getElementById('qCobre').value +
        '\\nPolos: ' + document.getElementById('qPolos').value +
        '\\nQuantidade: ' + document.getElementById('qQtd').value +
        '\\nTerra: ' + terraText +
        '\\nNeutro: ' + neutroText +
        '\\nCNPJ/CPF: ' + document.getElementById('qCnpj').value +
        '\\nNome: ' + document.getElementById('qNome').value +
        '\\nObservacao: ' + document.getElementById('qObs').value
    );
    window.open('https://wa.me/5511924898593?text=' + msg, '_blank');
});"""

    new_std = re.sub(old_js, new_js, new_std, flags=re.DOTALL)

    if new_std != std:
        write_file('barramento-padrao-din.html', new_std)
        print("  barramento-padrao-din.html: ATUALIZADO com novos cards!")
    else:
        print("  barramento-padrao-din.html: nao conseguiu substituir (verifique manualmente)")
else:
    print("  barramento-padrao-din.html: ja tem cards novos, verificando fotos...")
    # Garantir que foto bifasico 2 eh a principal
    if 'standard-bifasico-1.png" alt="Barramento Bif' in std:
        std = std.replace(
            'standard-bifasico-1.png" alt="Barramento Bif',
            'standard-bifasico-2.png" alt="Barramento Bif'
        )
        # Swap gallery thumbnails
        std = std.replace(
            'standard-bifasico-1.png" alt="Bifasico 1"',
            'TEMP_SWAP" alt="Bifasico 1"'
        )
        std = std.replace(
            'standard-bifasico-2.png" alt="Bifasico 2"',
            'standard-bifasico-1.png" alt="Bifasico 2"'
        )
        std = std.replace(
            'TEMP_SWAP" alt="Bifasico 1"',
            'standard-bifasico-2.png" alt="Bifasico 1"'
        )
        write_file('barramento-padrao-din.html', std)
        print("  Fotos bifasico invertidas!")

    # Atualizar fotos trifasico se ainda usa as antigas
    std = read_file('barramento-padrao-din.html')
    if 'barramento-trifasico-2.jpg' in std:
        std = std.replace('barramento-trifasico-2.jpg', 'standard-trifasico-1.png')
        std = std.replace('barramento-trifasico-1.jpg', 'standard-trifasico-2.png')
        std = std.replace('barramento-trifasico-4.jpg', 'standard-trifasico-2.png')
        write_file('barramento-padrao-din.html', std)
        print("  Fotos trifasico atualizadas!")
    else:
        print("  Fotos ja atualizadas")

# ============================================================
# 3) ATUALIZAR EMPRESA: NUMEROS
# ============================================================
print("\n--- EMPRESA ---")
emp = read_file('empresa.html')
changed = False

# Atualizar 500 -> 3000
if 'data-count="500"' in emp:
    emp = emp.replace('data-count="500"', 'data-count="3000"')
    changed = True
    print("  500 -> 3000 Projetos")

# Atualizar 15 -> 20 (nos numeros, nao no story)
# O number-value com data-count="15" esta na numbers-section
if '<div class="number-value" data-count="15">' in emp:
    emp = emp.replace(
        '<div class="number-value" data-count="15">',
        '<div class="number-value" data-count="20">'
    )
    changed = True
    print("  15 -> 20 Anos")

# Atualizar label "Anos de Experiencia" (manter)

# Atualizar 200 -> 1000
if 'data-count="200"' in emp:
    emp = emp.replace('data-count="200"', 'data-count="1000"')
    changed = True
    print("  200 -> 1000 Clientes")

# Atualizar 100% Satisfacao -> 0 Devolucoes
if 'data-count="100"' in emp:
    emp = emp.replace('data-count="100"', 'data-count="0"')
    emp = emp.replace('Satisfação Garantida', 'Devoluções')
    changed = True
    print("  100% Satisfacao -> 0 Devolucoes")

# Atualizar o story accent box tambem (15 -> 20 anos de mercado)
if '<div class="sab-number" data-count="15">' in emp:
    emp = emp.replace(
        '<div class="sab-number" data-count="15">',
        '<div class="sab-number" data-count="20">'
    )
    emp = emp.replace('Anos de Mercado', 'Anos de Mercado')
    print("  Story box: 15 -> 20 Anos")
    changed = True

# Corrigir o counter JS para lidar com valor 0
if "el.target.textContent=t+(t===100?'%':'+')" in emp:
    emp = emp.replace(
        "el.target.textContent=t+(t===100?'%':'+')",
        "el.target.textContent=t+(t===0?'':t===100?'%':'+')"
    )
    changed = True
    print("  Counter JS: fix para valor 0")
elif "t+(t===100?'%':'+')" in emp and "t===0" not in emp:
    # Try alternative pattern
    emp = emp.replace(
        "t+(t===100?'%':'+')",
        "t+(t===0?'':t===100?'%':'+')"
    )
    changed = True
    print("  Counter JS: fix para valor 0 (alt)")

if changed:
    write_file('empresa.html', emp)
    print("  empresa.html: SALVO!")
else:
    print("  empresa.html: nenhuma alteracao necessaria")

print("\n========================================")
print("PRONTO! Agora faca:")
print("  git add -A")
print('  git commit -m "Linha Standard + empresa numeros atualizados"')
print("  git push")
print("========================================")

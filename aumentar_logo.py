"""Aumenta o logo e o header em todas as paginas do site"""
import os

DIR = r"C:\Users\kauap\Documents\aepaineis-site"
CSS = os.path.join(DIR, "styles.css")

with open(CSS, 'r', encoding='utf-8') as f:
    css = f.read()

changed = False

# 1) Aumentar header de 100px para 120px
if '--header-h: 100px;' in css:
    css = css.replace('--header-h: 100px;', '--header-h: 120px;')
    changed = True
    print("[CSS] Header: 100px -> 120px")

# 2) Aumentar logo de 90px para 110px
if 'height:90px;width:auto;max-height:calc(var(--header-h) - 10px)' in css:
    css = css.replace(
        'height:90px;width:auto;max-height:calc(var(--header-h) - 10px)',
        'height:110px;width:auto;max-height:calc(var(--header-h) - 5px)'
    )
    changed = True
    print("[CSS] Logo: 90px -> 110px")

# 3) Diminuir logo do footer proporcionalmente (64 -> 80)
if 'filter:brightness(0) invert(1);height:64px' in css:
    css = css.replace(
        'filter:brightness(0) invert(1);height:64px',
        'filter:brightness(0) invert(1);height:80px'
    )
    changed = True
    print("[CSS] Logo footer: 64px -> 80px")

if changed:
    with open(CSS, 'w', encoding='utf-8') as f:
        f.write(css)
    print("\n  styles.css SALVO! (vale para todas as paginas)")
else:
    print("\n  Nenhuma alteracao necessaria")

print("\nAgora faca:")
print("  cd C:\\Users\\kauap\\Documents\\aepaineis-site")
print('  git add -A; git commit -m "Logo maior no header"; git push')

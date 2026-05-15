"""
Remove BEKPO logo from the orange document holder in quadro-porta-bipartida.png
Replaces the BEKPO text area with the orange background color of the holder.
"""
from PIL import Image, ImageDraw, ImageFilter
import os

# Paths
src = r"C:\Users\kauap\OneDrive\Documentos\aepaineis-site\Fotos quadros CATALOGO\QUADRO COM PORTA BIPARTIDA.png"
dst = r"C:\Users\kauap\Documents\aepaineis-site\img\quadro-porta-bipartida.png"

img = Image.open(src)
w, h = img.size
print(f"Image size: {w}x{h}")

# The BEKPO logo is on the orange document holder on the right door
# Based on the image, the logo is roughly in the upper portion of the orange envelope
# We need to find the exact coordinates. Let's sample the orange color first.

# The orange holder is approximately in the right half of the image
# BEKPO text appears to be around 58-72% from left, 48-55% from top (estimated from visual)
# Let's define the region more precisely based on image proportions

# For a ~600x600 image, BEKPO is roughly at:
# x: 350-430, y: 290-320 (approximate)
# But let's scale to actual dimensions

# Approximate relative coordinates of BEKPO text on the orange holder
# These are ratios of the full image
logo_left = int(w * 0.545)
logo_top = int(h * 0.465)
logo_right = int(w * 0.695)
logo_bottom = int(h * 0.52)

print(f"Logo region: ({logo_left}, {logo_top}) to ({logo_right}, {logo_bottom})")

# Sample the orange color from just below the logo area (pure orange, no text)
sample_x = int(w * 0.62)
sample_y = int(h * 0.58)
orange_color = img.getpixel((sample_x, sample_y))
print(f"Sampled orange color at ({sample_x},{sample_y}): {orange_color}")

# Create a draw object
draw = ImageDraw.Draw(img)

# Fill the BEKPO area with the sampled orange color
# Use a slightly larger area to ensure full coverage
padding = 5
draw.rectangle(
    [logo_left - padding, logo_top - padding, logo_right + padding, logo_bottom + padding],
    fill=orange_color[:3]  # Use RGB only
)

# Apply a slight blur to the patched area to blend edges
# Crop the region, blur it, paste it back
region = img.crop((logo_left - padding - 3, logo_top - padding - 3,
                    logo_right + padding + 3, logo_bottom + padding + 3))
region = region.filter(ImageFilter.GaussianBlur(radius=2))
img.paste(region, (logo_left - padding - 3, logo_top - padding - 3))

# Save
os.makedirs(os.path.dirname(dst), exist_ok=True)
img.save(dst, quality=95)
print(f"Saved to: {dst}")
print("Done! BEKPO logo removed.")

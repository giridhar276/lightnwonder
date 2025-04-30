
# Using Alpha Mask
from PIL import Image

img = Image.open("example.jpg").convert("RGBA")

# Split channels and reapply alpha
r, g, b, a = img.split()
img.putalpha(a)

img.save("with_alpha.png")
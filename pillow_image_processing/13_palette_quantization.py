
# Convert to palette image
from PIL import Image

img = Image.open("example.jpg")
palette_img = img.convert("P", palette=Image.ADAPTIVE, colors=16)
palette_img.save("palette_image.png")

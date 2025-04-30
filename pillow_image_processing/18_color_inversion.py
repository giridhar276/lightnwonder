
# Invert image colors
from PIL import Image, ImageOps

img = Image.open("example.jpg")
inverted = ImageOps.invert(img.convert("RGB"))
inverted.save("inverted_colors.jpg")

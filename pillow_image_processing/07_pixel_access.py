
# Pixel Access
from PIL import Image

img = Image.open("example.jpg")
pixels = img.load()

# Invert pixels
for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]
        pixels[i, j] = (255 - r, 255 - g, 255 - b)

img.save("inverted.jpg")

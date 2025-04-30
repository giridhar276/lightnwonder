
# Simulated edge detection
from PIL import Image, ImageFilter

img = Image.open("example.jpg")
edges = img.filter(ImageFilter.FIND_EDGES)
edges.save("edges.jpg")

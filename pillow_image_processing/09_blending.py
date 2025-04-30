

from PIL import Image

# Open two images and resize to same size
img1 = Image.open("example.jpg").resize((300, 300))
img2 = Image.open("example2.jpg").resize((300, 300))

# Blend with alpha (0.5 means equal weight)
blended = Image.blend(img1, img2, alpha=0.5)
blended.save("blended.jpg")
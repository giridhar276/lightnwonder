
from PIL import Image, ImageDraw, ImageFont

img = Image.open("example.jpg")
draw = ImageDraw.Draw(img)

# Draw text at position (x, y)
draw.text((10, 10), "Hello, puppy]!", fill="white")

img.save("text_overlay.jpg")
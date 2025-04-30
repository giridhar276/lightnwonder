
# Add watermark to image
from PIL import Image, ImageDraw, ImageFont

base = Image.open("example.jpg").convert("RGBA")
watermark = Image.new("RGBA", base.size)

draw = ImageDraw.Draw(watermark)
text = "giri"

# Use default font and draw watermark text
font = ImageFont.load_default()
draw.text((10, 10), text, fill=(255, 255, 255, 128), font=font)

# Overlay watermark onto base image
combined = Image.alpha_composite(base, watermark)
combined.save("watermarked.png")
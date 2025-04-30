
# Create contact sheet from thumbnails
from PIL import Image
import os

thumbs = []
folder = "images"
for file in os.listdir(folder):
    if file.endswith(".jpg"):
        img = Image.open(os.path.join(folder, file))
        img.thumbnail((100, 100))
        thumbs.append(img)

contact_sheet = Image.new("RGB", (500, 100 * len(thumbs)//5 + 1))

x = y = 0
for i, thumb in enumerate(thumbs):
    contact_sheet.paste(thumb, (x, y))
    x += 100
    if (i + 1) % 5 == 0:
        x = 0
        y += 100

contact_sheet.save("contact_sheet.jpg")


# Generate QR code and combine with image
import qrcode
from PIL import Image

qr = qrcode.make("https://www.google.com")
img = Image.open("example.jpg")

# Resize and paste QR on image
qr = qr.resize((100, 100))
img.paste(qr, (img.width - 110, img.height - 110))
img.save("image_with_qr.jpg")

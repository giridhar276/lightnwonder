
from PIL import Image

img = Image.open("example.jpg")

# Crop: (left, upper, right, lower) pixel coordinates
cropped = img.crop((100, 100, 400, 400))
cropped.save("cropped.jpg")

# Resize: specify new width and height
resized = img.resize((200, 200))
resized.save("resized.jpg")

# Rotate: specify degrees counterclockwise
rotated = img.rotate(90)
rotated.save("rotated.jpg")
from PIL import Image

img = Image.open("example.jpg")

# Convert to grayscale (L mode)
gray_img = img.convert("L")
gray_img.save("gray_image.jpg")
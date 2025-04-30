
# Apply affine transform (scale + translate)
from PIL import Image

img = Image.open("example.jpg")
affine_img = img.transform(img.size, Image.AFFINE, (1, 0, 100, 0, 1, 50))
affine_img.save("affine_transformed.jpg")

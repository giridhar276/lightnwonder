# Import the Image module from Pillow
from PIL import Image

# Open an existing image
img = Image.open("example.jpg")

# Display the image
img.show()

# Save the image in a different format
img.save("output_image.png")
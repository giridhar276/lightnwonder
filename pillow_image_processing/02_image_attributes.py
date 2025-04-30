from PIL import Image

img = Image.open("example.jpg")

# Print important image attributes
print("Format:", img.format)  # e.g., JPEG, PNG
print("Size:", img.size)      # (width, height)
print("Mode:", img.mode)      # RGB, RGBA, L (grayscale), etc.
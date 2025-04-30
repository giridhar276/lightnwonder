


from PIL import Image, ImageFilter, ImageEnhance

img = Image.open("example.jpg")

# Apply a blur filter
blurred = img.filter(ImageFilter.BLUR)
blurred.save("blurred.jpg")

# Enhance contrast
enhancer = ImageEnhance.Contrast(img)
enhanced = enhancer.enhance(2.0)  # 2x contrast
enhanced.save("contrast_enhanced.jpg")

# Batch Convert Images in Folder
from PIL import Image
import os

input_folder = "images"
output_folder = "converted"
os.makedirs(output_folder, exist_ok=True)

# Convert all .png images to .jpg in folder
for file in os.listdir(input_folder):
    if file.endswith(".jpg"):
        img = Image.open(os.path.join(input_folder, file))
        img = img.convert("RGB")
        output_path = os.path.join(output_folder, file.replace(".jpg", ".png"))
        img.save(output_path)
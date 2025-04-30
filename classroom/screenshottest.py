#pip install pillow  # one single iamge
from PIL import ImageGrab  
screenshot = ImageGrab.grab()
screenshot.save('my_image.png', 'PNG')

#pip install pillow
from PIL import ImageGrab
import time
for val in range(1,20):
    filename = "image_" + str(val) + ".png"
    screenshot = ImageGrab.grab()
    time.sleep(2)
    print(filename,"generated")
    screenshot.save(filename, 'PNG')

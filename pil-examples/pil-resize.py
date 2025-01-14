from PIL import Image
import matplotlib.pyplot as plt


image = Image.open("lena.tif")

plt.figure(figsize=(5,5))
image_small = image.resize((64, 64))

plt.imshow(image_small)
plt.show()

image_small.save('lena_small.tif')
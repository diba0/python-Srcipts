from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("lena.tif")
img1 = Image.open('lena.jpg')
img2 = Image.open('lena.bmp')

plt.figure(figsize=(15,5))

plt.subplot(131)
plt.axis('off')
plt.imshow(image)
plt.title(image.format)

plt.subplot(132)
plt.axis('off')
plt.imshow(img1)
plt.title(img1.format)

plt.subplot(133)
plt.axis('off')
plt.imshow(img2)
plt.title(img2.format)

plt.show()
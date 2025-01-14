from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("lena.tif")
img_r, img_g, img_b = image.split()
plt.figure(figsize=(10,10))

plt.subplot(221)
plt.axis('off')
plt.imshow(img_r, cmap='Reds')
plt.title('Red channel')

plt.subplot(222)
plt.axis('off')
plt.imshow(img_g, cmap='Greens')
plt.title('Green channel')

plt.subplot(223)
plt.axis('off')
plt.imshow(img_b, cmap='Blues')
plt.title('Blue channel')

img_rgb = Image.merge('RGB', (img_r, img_g, img_b))
plt.subplot(224)
plt.axis('off')
plt.imshow(img_rgb)
plt.title('RGB')

plt.show()
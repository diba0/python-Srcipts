from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('lena.tif')

img_gray = img.convert('L')
print('mode:', img_gray.mode)

plt.figure(figsize=(5,5))
plt.imshow(img_gray, cmap='gray')
plt.show()

img_gray.save('lena_gray.bmp')
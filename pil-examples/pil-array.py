from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_gray = Image.open("lena_gray.bmp")
arr_image_gray = np.array(image_gray)
print('image_gray:', arr_image_gray.shape, arr_image_gray.dtype)
print(arr_image_gray)

image = Image.open("lena.tif")
arr_image = np.array(image)
print('image:', arr_image.shape, arr_image.dtype)
print(arr_image)

arr_img_new = 255 - arr_image_gray

plt.figure(figsize=(10,5))

plt.subplot(121)
plt.axis('off')
plt.imshow(arr_image_gray, cmap='gray')

plt.subplot(122)
plt.axis('off')
plt.imshow(arr_img_new, cmap='gray')

plt.show()
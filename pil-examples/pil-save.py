from PIL import Image

image = Image.open("lena.tif")

image.save('lena.jpg')
image.save('lena.bmp')

img1 = Image.open('lena.jpg')
img2 = Image.open('lena.bmp')

print('image:', image.format, image.size, image.mode)
print('img1:', img1.format, img1.size, img1.mode)
print('img2:', img2.format, img2.size, img2.mode)
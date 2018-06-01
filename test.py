from PIL import Image


lena = Image.open("lena.png")
w, h = lena.size
lena.thumbnail((w // 2, h // 2))
lena_YCbCr = lena.convert('YCbCr')
lena_Y, lena_Cb, lena_Cr = lena_YCbCr.split()
lena.save('lena_rgb.png')
lena_Y.save("lena_Y.jpg")
lena_Cb.save("lena_Cb.jpg")
lena_Cr.save("lena_Cr.jpg")

'''
Expt No. 1: 

Title: Introduction to Digital Image Processing using Python 

Aim: To write a program using Python to perform the following:
i) Read an image
ii) Display an image
iii) Create an image
iv) Display the following information about an image:
     a) Size of the image in terms of rows and columns of pixels
     b) No. of bits per pixel
     c) Size of the entire image in terms of memory requirements
v) View the entire image as a 2-D array of stored intensity levels.
vi) View a partial image as a 2-D array of stored intensity levels.
'''
# Important Imports
import numpy as np
from matplotlib import pyplot as plt


### i) Read an image
img=plt.imread('CH01\Fig0101(1921 digital image).tif')


### ii) Display an image
plt.figure(1)
plt.imshow(img,cmap='gray')
plt.show()
plt.imsave('input_output\expt1_original_img.jpg',img,cmap='gray')

### iii) Create a random image
plt.figure(2)
rand_img=np.random.randint(0,255,(5,5),dtype='uint8')
plt.imshow(np.random.randint(0,255,(5,5)),cmap='gray')
plt.savefig('input_output\expt1_random_img.jpg',dpi=300)
plt.show()


### iv) Display the following information about an image:

##### a) Size of the image in terms of rows and columns of pixels
r,c=rand_img.shape
print(f"Image Size: Rows={r}, Columns={c}")


##### b) No. of bits per pixel
'''
Size of an image = rows * cols * bpp,
where bpp is bits per pixel
'''
size_of_img=rand_img.size*rand_img.itemsize
bpp=size_of_img/(r*c)
print(f"Bits Per Pixel = {bpp*8} bits")


##### c) Size of the entire image in terms of memory requirements
print(f"Size of image = {size_of_img} bytes")


### v) View the entire image as a 2-D array of stored intensity levels
print("Entire image as 2-D array if stored intensity levels:")
print(rand_img)


### vi) View a partial image as a 2-D array of stored intensity levels.
print("Partial image as 2-D array if stored intensity levels:")
print(rand_img[:4,:3])

'''
Title: Point and Neighbourhood Operations in Digital Image Processing using Python

Aim: To write a program using Python to perform the following:
     a) Intensity Transformation to obtain the negative of an 8-bit image using Point Processing
     b) Local Blurring using Neighbourhood Processing
'''
# Important imports:
import numpy as np
from matplotlib import pyplot as plt, gridspec as gs


# a) Intensity Transformation to obtain the negative of an 8-bit image using Point Processing

img1=plt.imread('CH02\Fig0232(a)(partial_body_scan).tif')

def neg_img(img1):
    ### Creating an image with all intensity values as 255
    white_img=np.uint8(np.ones(img1.shape)*255)
    return white_img-img1

# plots:
fig1=plt.figure(1)
gs1=gs.GridSpec(1,2)
ax11=plt.subplot(gs1[0,0])
ax11.set_title("Original Image")
ax11.axis("off")
ax11.imshow(img1,cmap='gray')

ax12=plt.subplot(gs1[0,1])
ax12.set_title("Negative Image")
ax12.axis("off")
ax12.imshow(neg_img(img1),cmap='gray')

plt.suptitle('Intensity Transformation to obtain the negative of an 8-bit image using Point Processing',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
fig1.set_size_inches(10, 8)
plt.savefig('input_output/expt6_a.jpg',dpi=300,)
fig1.set_size_inches(5, 4)
plt.show()



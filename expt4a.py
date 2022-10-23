'''
Expt No. 4:

Title: Image Interpolation using Python

Aim: To implement the following Interpolation Techniques:
     a) Nearest Neighbour Interpolation Technique (refer diptools.py for algorithm)
        -> To resize barcodes
     b) Bilinear Interpolation Technique (Used builtin library function : openCV)
     c) Bicubic Interpolation Technique  (Used builtin library function : openCV)

Notes:
fx:   Scaling factor of x
fy:   Scaling factor of y

'''

# Important Imports:
from skimage import io 
import numpy as np
from matplotlib import pyplot as plt, gridspec as gs
from dip_toolbox import DipTools
import cv2 as cv

# Creating DipTools class
dip=DipTools()


# Creating our own image
img1=np.random.randint(0,255,(8,8))
img3=np.float32(img1)


# importing a colored image
img2=io.imread('extra_images\original_img.jpg')


# Nearest Neighbourhood interpolation

fig1=plt.figure(1)
gs1=gs.GridSpec(2,6)

ax11=plt.subplot(gs1[0:1,0:2])
ax11.set_title("Original Image")
ax11.imshow(img1)

ax12=plt.subplot(gs1[0:2,2:6])
ax12.set_title("Zoomed Image")
ax12.imshow(dip.nearest_neighbourhood(img1,(100,100)))

ax13=plt.subplot(gs1[1:2,0:2])
ax13.set_title("Shrinked Image")
ax13.imshow(dip.nearest_neighbourhood(img1,(4,4)))

plt.suptitle('Nearest Neigbourhood Interpolation',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
plt.savefig('input_output\expt4a_concept_nn.jpg',dpi=300)
plt.show()


# Bilinear interpolation

fig2=plt.figure(2)
gs2=gs.GridSpec(2,6)

ax21=plt.subplot(gs2[0:1,0:2])
ax21.set_title("Original Image")
ax21.imshow(img1)

ax22=plt.subplot(gs2[0:2,2:6])
ax22.set_title("Zoomed Image")
ax22.imshow(cv.resize(img3,None,fx=12.5,fy=12.5,interpolation=cv.INTER_LINEAR))

ax23=plt.subplot(gs2[1:2,0:2])
ax23.set_title("Shrinked Image")
ax23.imshow(cv.resize(img3,None,fx=0.5,fy=0.5,interpolation=cv.INTER_LINEAR))

plt.suptitle('Bilinear Interpolation',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
plt.savefig('input_output\expt4a_concept_bl.jpg',dpi=300)
plt.show()


# Bilcubic interpolation

fig3=plt.figure(3)
gs3=gs.GridSpec(2,6)

ax31=plt.subplot(gs3[0:1,0:2])
ax31.set_title("Original Image")
ax31.imshow(img1)

ax32=plt.subplot(gs3[0:2,2:6])
ax32.set_title("Zoomed Image")
ax32.imshow(cv.resize(img3,None,fx=12.5,fy=12.5,interpolation=cv.INTER_CUBIC))

ax33=plt.subplot(gs3[1:2,0:2])
ax33.set_title("Shrinked Image")
ax33.imshow(cv.resize(img3,None,fx=0.5,fy=0.5,interpolation=cv.INTER_CUBIC))

plt.suptitle('Bicubic Interpolation',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
plt.savefig('input_output\expt4a_concept_bc.jpg',dpi=300)
plt.show()


# Comparison of Interpolation Techniques:
### Zooming (50*50)

fig4=plt.figure(4)
gs4=gs.GridSpec(2,2)

ax41=plt.subplot(gs4[0:1,0:1])
ax41.set_title("Original Image")
ax41.imshow(img1)

ax42=plt.subplot(gs4[0:1,1:2])
ax42.set_title("Nearest Neighbourhood")
ax42.imshow(dip.nearest_neighbourhood(img1,(50,50)))

ax43=plt.subplot(gs4[1:2,0:1])
ax43.set_title(" Bilinear Interpolation")
ax43.imshow(cv.resize(img3,None,fx=6.25,fy=6.25,interpolation=cv.INTER_LINEAR))

ax43=plt.subplot(gs4[1:2,1:2])
ax43.set_title("Bicubic Interpolation")
ax43.imshow(cv.resize(img3,None,fx=6.25,fy=6.25,interpolation=cv.INTER_CUBIC))

plt.suptitle('Comparison of Interpolation Techniques in zooming (50*50)',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
plt.savefig('input_output\expt4a_comparison_zooming.jpg',dpi=300)
plt.show()


# Comparison of Interpolation Techniques:
### Shrinking (4*4)

fig5=plt.figure(5)
gs5=gs.GridSpec(2,2)

ax51=plt.subplot(gs5[0:1,0:1])
ax51.set_title("Original Image")
ax51.imshow(img1)

ax52=plt.subplot(gs5[0:1,1:2])
ax52.set_title("Nearest Neighbourhood")
ax52.imshow(dip.nearest_neighbourhood(img1,(4,4)))

ax53=plt.subplot(gs5[1:2,0:1])
ax53.set_title("Bilinear Interpolation")
ax53.imshow(cv.resize(img3,None,fx=0.5,fy=0.5,interpolation=cv.INTER_LINEAR))

ax53=plt.subplot(gs5[1:2,1:2])
ax53.set_title("Bicubic Interpolation")
ax53.imshow(cv.resize(img3,None,fx=0.5,fy=0.5,interpolation=cv.INTER_CUBIC))

plt.suptitle('Comparison of Interpolation Techniques in shrinking (4*4)',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
plt.savefig('input_output\expt4a_comparison_shrinking.jpg',dpi=300)
plt.show()



# Applying the Nearest Neighbourhood algorithm on actual images:
zimg=dip.nearest_neighbourhood(img2,(2000,3000,3))
simg=dip.nearest_neighbourhood(img2,(200,300,3))

### Displaying Images
plt.figure(6)
plt.title(f'Original Image {img2.shape[0:2]}')
io.imshow(img2)
plt.figure(7)
plt.title(f'Zoomed Image {zimg.shape[0:2]}')
io.imshow(zimg)
plt.figure(8)
plt.title(f'Shrinked Image {simg.shape[0:2]}')
io.imshow(simg)

plt.show()

### Saving Output Images
io.imsave('input_output\expt4a_original_img_1795_2666.jpg',img2)
io.imsave('input_output\expt4a_shrinked_img_200_300.jpg',simg)
io.imsave('input_output\expt4a_zoomed_img_2000_3000.jpg',zimg)
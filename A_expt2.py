'''
A_expt No. 2: 

Title: Bit Plane Slicing 

Aim: To write a program using Python to perform bit plane slicing to visualize False Contouring

Note: For the program of bitplane slicing, refer diptools.py

'''

from matplotlib import pyplot as plt, gridspec as gs
from dip_toolbox import IntensityTransformations

# importing image
img1=plt.imread('CH02\Fig0221(a)(ctskull-256).tif')


# creating object of class IntensityTransformations
it=IntensityTransformations()


# Getting image in each bit plane:
img_bps=it.bit_plane_slicing(img1)


# Displaying single bit images:
fig1=plt.figure(1)
gs1=gs.GridSpec(2,6)

ax11=plt.subplot(gs1[0:2,0:2])
ax11.set_title("Original Image")
ax11.axis("off")
ax11.imshow(img1,cmap='gray')

ax12=plt.subplot(gs1[0,2])
ax12.set_title("Bitplanes:7")
ax12.axis("off")
ax12.imshow((img1-img_bps[0]),cmap='gray')

ax13=plt.subplot(gs1[0,3])
ax13.set_title("Bitplanes:6")
ax13.axis("off")
ax13.imshow((img1-img_bps[0]-img_bps[1]),cmap='gray')

ax14=plt.subplot(gs1[0,4])
ax14.set_title("Bitplanes:5")
ax14.axis("off")
ax14.imshow((img1-img_bps[0]-img_bps[1]-img_bps[2]),cmap='gray')

ax15=plt.subplot(gs1[0,5])
ax15.set_title("Bitplanes:4")
ax15.axis("off")
ax15.imshow((img1-img_bps[0]-img_bps[1]-img_bps[2]-img_bps[3]),cmap='gray')

ax16=plt.subplot(gs1[1,2])
ax16.set_title("Bitplanes:3")
ax16.axis("off")
ax16.imshow((img1-img_bps[0]-img_bps[1]-img_bps[2]-img_bps[3]-img_bps[4]),cmap='gray')


ax17=plt.subplot(gs1[1,3])
ax17.set_title("Bitplanes:2")
ax17.axis("off")
ax17.imshow((img1-img_bps[0]-img_bps[1]-img_bps[2]-img_bps[3]-img_bps[4]-img_bps[5]),cmap='gray')

ax18=plt.subplot(gs1[1,4])
ax18.set_title("Bitplanes:1")
ax18.axis("off")
ax18.imshow((img1-img_bps[0]-img_bps[1]-img_bps[2]-img_bps[3]-img_bps[4]-img_bps[5]-img_bps[6]),cmap='gray')


plt.suptitle('Bit Plane Slicing to visualize False Contouring',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=1.2)
plt.savefig('input_output/A_expt2.jpg',dpi=300,)
plt.show()


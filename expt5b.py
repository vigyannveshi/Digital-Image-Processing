''' b) Image Subtraction for Enhancing Differences '''


# Important imports:
from dip_toolbox import DipTools
from matplotlib import pyplot as plt, gridspec as gs
import numpy as np


# importing image
img2=plt.imread('CH02\Fig0227(a)(washington_infrared).tif')


# importing class DipTools
dip=DipTools()
bp_img2=dip.bit_plane_slicing(img2)


img3=sum(bp_img2[1:7])


# plots
fig2=plt.figure(2)
gs2=gs.GridSpec(1,2)

ax21=plt.subplot(gs2[0,0])
ax21.set_title("Original Image")
ax21.axis("off")
ax21.imshow(img2,cmap='gray')

ax22=plt.subplot(gs2[0,1])
ax22.set_title("The LSB of every pixel in original image is set to zero")
ax22.axis("off")
ax22.imshow(img3,cmap='gray')

plt.suptitle('Image Subtraction for Enhancing Differences',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=1.2)
fig2.set_size_inches(10, 8)
plt.savefig('input_output/expt5_b.jpg',dpi=300,)
fig2.set_size_inches(5, 4)
plt.show()
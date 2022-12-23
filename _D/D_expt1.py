'''

D_expt No. 1: 

Title: Visualizing Aliasing  

Aim: To write a program using Python to visualize aliasing by
I) Result of resizing the image to 50% of its original size by pixel deletion using nearest neighbourhood
    i)  without blurring
    ii) after blurring with 3*3 averaging filter

II) Result of resizing the image to 25% of its original size using bilinear interpolation
    i) without blurring
    ii) after blurring with 5*5 averaging filter


'''

# important imports 

import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import cv2 as cv

### adding path to dip_toolbox
import sys
sys.path.append('./')

from dip_toolbox import Filters

# objects using Filters and Interpolation class
flt=Filters()

img1=plt.imread('CH04\Fig0417(a)(barbara).tif')
img2=plt.imread('CH04\Fig0418(a)(ray_traced_bottle_original).tif')

# plots
fig1=plt.figure(1)
gs1=gs.GridSpec(1,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[0,1])
ax12.set_title(f'shrinking to (50%) using (NN) without blurring')
ax12.axis('off')
ax12.imshow(cv.resize(img1,None,fx=0.5,fy=0.5,interpolation=cv.INTER_NEAREST),cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[0,2])
ax13.set_title(f'shrinking to (50%) using (NN) with 3*3 averaging')
ax13.axis('off')
ax13.imshow(cv.resize(flt.flt_apply(img1,3,flt.am_flt),None,fx=0.5,fy=0.5,interpolation=cv.INTER_NEAREST),cmap='gray',vmax=255,vmin=0)

fig1.tight_layout(pad=2)
fig1.set_size_inches(13,8)
fig1.suptitle('Visualizing Aliasing',font='Times New Roman',fontweight="bold",fontsize=16)
fig1.savefig('input_output/D_expt1_1.jpg',dpi=500)

fig2=plt.figure(2)
gs2=gs.GridSpec(1,3)

ax21=plt.subplot(gs2[0,0])
ax21.set_title('Original image')
ax21.axis('off')
ax21.imshow(img2,cmap='gray',vmax=255,vmin=0)

ax22=plt.subplot(gs2[0,1])
ax22.set_title(f'shrinking to (25%) using (BL) without blurring')
ax22.axis('off')
ax22.imshow(cv.resize(img2,None,fx=0.25,fy=0.25,interpolation=cv.INTER_LINEAR),cmap='gray')

ax23=plt.subplot(gs2[0,2])
ax23.set_title(f'shrinking to (25%) using (BL) with 5*5 averaging')
ax23.axis('off')
ax23.imshow(cv.resize(flt.flt_apply(img2,5,flt.am_flt),None,fx=0.25,fy=0.25,interpolation=cv.INTER_LINEAR),cmap='gray')

fig2.tight_layout(pad=2)
fig2.set_size_inches(13,8)
fig2.suptitle('Visualizing Aliasing',font='Times New Roman',fontweight="bold",fontsize=16)
fig2.savefig('input_output/D_expt1_2.jpg',dpi=500)

plt.show()
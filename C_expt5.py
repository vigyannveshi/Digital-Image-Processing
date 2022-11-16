'''
C_expt No. 5: 

Title: Handling Combination of additive Uniform noise with Salt & Pepper noise

Aim: To write a program using Python to add uniform noise and combine it with salt and  pepper noise to an original image, then apply filters and check their performance
i)   Arithmetic Mean Filter  (5*5) 
ii)  Geometric Mean Filter  (5*5)
iii) Median Filter (5*5)
iv)  Alpha-trimmed Mean Filter (5*5), d=5

'''


# important imports:
import numpy as np
from matplotlib import pyplot as plt,gridspec as gs
from dip_toolbox import NoiseModels, Filters

# creating objects from NoiseModels and Filters class:
nm=NoiseModels()
flt=Filters()

# importing original image:
img1=plt.imread('CH05\Fig0507(a)(ckt-board-orig).tif')

# adding Uniform noise (variance=800, mean=0), Salt & Pepper noise (Pp=Ps=0.1):
un=nm.uniform_noise(img1.shape,-np.sqrt(2400),np.sqrt(2400))
img_un=nm.add_noise(un,img1)
noisy_img=nm.salt_pepper_noise(img_un,0.1,0.1)

# filtering the noisy image using various filters:

### i)   Arithmetic Mean Filter  (5*5) 
flt_am_img=flt.flt_apply(noisy_img,5,flt.am_flt)

### ii)  Geometric Mean Filter  (5*5)
flt_gm_img=flt.flt_apply(noisy_img,5,flt.gm_flt,pad_with=255)

### iii) Median Filter  (5*5)
flt_md_img=flt.flt_apply(noisy_img,5,flt.median_flt)

### iv)  Alpha-trimmed Mean Filter (5*5), d=5
d=5
flt_alptrm_img=flt.flt_apply(noisy_img,5,flt.alptrm_flt(d))


# plots
fig1=plt.figure(1)
gs1=gs.GridSpec(2,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[0,1])
ax12.set_title(f'img + u($\mu$=0,$\sigma^2$=800) + sp(pp=ps=0.1)')
ax12.axis('off')
ax12.imshow(noisy_img,cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[0,2])
ax13.set_title(f'Filtered using AMF (5*5)')
ax13.axis('off')
ax13.imshow(flt_am_img,cmap='gray',vmax=255,vmin=0)


ax14=plt.subplot(gs1[1,0])
ax14.set_title(f'Filtered using GMF (5*5)')
ax14.axis('off')
ax14.imshow(flt_gm_img,cmap='gray',vmax=255,vmin=0)

ax15=plt.subplot(gs1[1,1])
ax15.set_title(f'Filtered using MDF (5*5)')
ax15.axis('off')
ax15.imshow(flt_md_img,cmap='gray',vmax=255,vmin=0)

ax16=plt.subplot(gs1[1,2])
ax16.set_title(f'Filtered using ALPTRMF (5*5) d={d}')
ax16.axis('off')
ax16.imshow(flt_alptrm_img,cmap='gray',vmax=255,vmin=0)

fig1.tight_layout(pad=2.5)
fig1.set_size_inches(13,8)
fig1.suptitle('Handling Combination of additive Uniform noise with Salt & Pepper noise',font='Times New Roman',fontweight="bold",fontsize=16)
fig1.savefig('input_output/C_expt5.jpg',dpi=500)
plt.show()


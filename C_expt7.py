'''
C_expt No. 7: 

Title: Handling Additive Gaussian noise with high variance using Adaptive Local Noise Reduction Filter 

Aim: To write a program using Python to add  Gaussian noise to an original image with higher variance, and appreciate the filtering difference between different filters:
i)   Arithmetic Mean Filter (7*7)
ii)  Geometric Mean Filter (7*7)
iii) Harmonic Mean Filter (7*7)
iv)  Adaptive Local Noise Reduction Filter (7*7, locality = 7*7)

'''

# important imports:
from matplotlib import pyplot as plt,gridspec as gs
from dip_toolbox import NoiseModels, Filters

# creating objects from NoiseModels and Filters class:
nm=NoiseModels()
flt=Filters()

# importing original image:
img1=plt.imread('CH05\Fig0507(a)(ckt-board-orig).tif')

# Adding Gaussian Noise with high variance
mean=0
var=1000
gn=nm.gaussian_noise(img1.shape,mean,var)
img_gn=nm.add_noise(gn,img1)

# Applying filters:
ord=7
flt_am_img=flt.flt_apply(img_gn,ord,flt.am_flt,pad_with=255)
flt_gm_img=flt.flt_apply(img_gn,ord,flt.gm_flt,pad_with=255)
flt_hm_img=flt.flt_apply(img_gn,ord,flt.hm_flt,pad_with=255)
flt_alnr_img=flt.adpt_lclnr_flt(img_gn,ord,var,pad_with=255)

# plots:
fig1=plt.figure(1)
gs1=gs.GridSpec(2,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[0,1])
ax12.set_title(f'img + gn($\mu$={mean},$\sigma^2$={var})')
ax12.axis('off')
ax12.imshow(img_gn,cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[0,2])
ax13.set_title(f'Filtered using AMF ({ord}*{ord})')
ax13.axis('off')
ax13.imshow(flt_am_img,cmap='gray',vmax=255,vmin=0)


ax14=plt.subplot(gs1[1,0])
ax14.set_title(f'Filtered using GMF ({ord}*{ord})')
ax14.axis('off')
ax14.imshow(flt_gm_img,cmap='gray',vmax=255,vmin=0)

ax15=plt.subplot(gs1[1,1])
ax15.set_title(f'Filtered using HMF ({ord}*{ord})')
ax15.axis('off')
ax15.imshow(flt_hm_img,cmap='gray',vmax=255,vmin=0)

ax16=plt.subplot(gs1[1,2])
ax16.set_title(f'Filtered using ALNRF ({ord}*{ord})')
ax16.axis('off')
ax16.imshow(flt_alnr_img,cmap='gray',vmax=255,vmin=0)

fig1.tight_layout(pad=2.5)
fig1.set_size_inches(13,8)
fig1.suptitle('Handling Additive Gaussian noise with high variance using Adaptive Local Noise Reduction Filter',font='Times New Roman',fontweight="bold",fontsize=16)
fig1.savefig('input_output/C_expt7.jpg',dpi=500)
plt.show()

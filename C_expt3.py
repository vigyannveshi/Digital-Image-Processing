'''
C_expt No. 3: 

Title: Handling salt and pepper noise using Contraharmonic mean filters

Aim: To write a program using Python to add only salt and only pepper noise to  an original image, then apply filters and check their performance
i)    Contraharmonic mean filter (q=1.5)(3*3) on pepper noise
ii)   Contraharmonic mean filter (q=-1.5)(3*3) on salt noise
iii)  Contraharmonic mean filter (q=-1.5)(3*3) on pepper noise
iv)   Contraharmonic mean filter (q=1.5)(3*3) on salt noise


'''

# important imports
from matplotlib import pyplot as plt, gridspec as gs
from dip_toolbox import NoiseModels, Filters
import cv2 as cv


# importing image and addition of Gaussian noise:
img1=plt.imread('CH05\Fig0507(a)(ckt-board-orig).tif')

nm=NoiseModels()
mean=0;var=500
sn_img=nm.salt_pepper_noise(img1,pp=0,ps=0.1)
pn_img=nm.salt_pepper_noise(img1,pp=0.1,ps=0)


# creating object from Filters class
imf=Filters()


# plots
fig1=plt.figure(1)
gs1=gs.GridSpec(2,4)

ax11=plt.subplot(gs1[0,0:2])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[0,2:3])
ax12.set_title(f'Salt Noise (p=0.1)')
ax12.axis('off')
ax12.imshow(sn_img,cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[0,3:4])
ax13.set_title(f'Pepper Noise (p=0.1)')
ax13.axis('off')
ax13.imshow(pn_img,cmap='gray',vmax=255,vmin=0)


ax14=plt.subplot(gs1[1,0])
ax14.set_title(f'CHM (q=1.5)(3*3) on PN (p=0.1)')
ax14.axis('off')
ax14.imshow(imf.flt_apply(pn_img,ord=3,flt=imf.chm_flt(5),pad_with=255),cmap='gray',vmax=255,vmin=0)

ax15=plt.subplot(gs1[1,1])
ax15.set_title(f'CHM (q=-1.5)(3*3) on SN (p=0.1)')
ax15.axis('off')
ax15.imshow(imf.flt_apply(sn_img,ord=3,flt=imf.chm_flt(-1.5),pad_with=255),cmap='gray',vmax=255,vmin=0)

ax16=plt.subplot(gs1[1,2])
ax16.set_title(f'CHM (q=-1.5)(3*3) on PN (p=0.1)')
ax16.axis('off')
ax16.imshow(imf.flt_apply(pn_img,ord=3,flt=imf.chm_flt(-1.5),pad_with=255),cmap='gray',vmax=255,vmin=0)

ax17=plt.subplot(gs1[1,3])
ax17.set_title(f'CHM (q=1.5)(3*3) on SN (p=0.1)')
ax17.axis('off')
ax17.imshow(imf.flt_apply(sn_img,ord=3,flt=imf.chm_flt(1.5),pad_with=255),cmap='gray',vmax=255,vmin=0)

fig1.tight_layout(pad=2.5)
fig1.set_size_inches(13,8)
fig1.suptitle('Handling salt and pepper noise filters (3*3) ',font='Times New Roman',fontweight="bold",fontsize=16)
fig1.savefig('input_output/C_expt3.jpg',dpi=500)
plt.show()


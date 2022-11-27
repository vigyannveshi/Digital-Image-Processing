'''
C_expt No. 8: 

Title: Visualizing the Atmospheric Turbulence Degradation in an image in the spatial as well as the frequency domain

Aim: To write a program using Python to visualize the effect of Atmospheric Turbulence Degradation {H(u,v)=e^(-k)((u-M/2)^2+(v-N/2)^2) :Hufnagel - Stanley 1964} in the spatial and frequency Domain
for different values of k:
1) k=0.0025 (Severe Turbulence)
2) k=0.001  (Mild Turbulence)
3) k=0.00025 (Low Turbulence)
'''

# important imports:
import numpy as np
from matplotlib import pyplot as plt,gridspec as gs
from dip_toolbox import FrequencyDomain,DegradationModels,IntensityTransformations

# creating objects from the classes imported:
fd=FrequencyDomain()
dm=DegradationModels()
it=IntensityTransformations()

# importing the original image:
img1=plt.imread('CH05\Fig0525(a)(aerial_view_no_turb).tif')
img1_f=fd.dftshift2(fd.dft2(img1))

# atmospheric turbulence degradation:
H_st=dm.atm_tur(img1.shape,0.0025)    # Severe Turbulence
H_mt=dm.atm_tur(img1.shape,0.001)     # Mild Turbulence
H_lt=dm.atm_tur(img1.shape,0.00025)   # Low Turbulence

# degraded images in frequency domain:
img_f_H_st=img1_f*H_st
img_f_H_mt=img1_f*H_mt
img_f_H_lt=img1_f*H_lt

# degraded images in spatial domain:
img_s_H_st=fd.idft2(fd.dftshift2(img_f_H_st))
img_s_H_mt=fd.idft2(fd.dftshift2(img_f_H_mt))
img_s_H_lt=fd.idft2(fd.dftshift2(img_f_H_lt))



# plots
fig1=plt.figure(1)
gs1=gs.GridSpec(2,4)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[0,1])
ax12.set_title(f'k=0.0025 (Severe Turbulence)')
ax12.axis('off')
ax12.imshow(img_s_H_st,cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[0,2])
ax13.set_title(f'k=0.001  (Mild Turbulence)')
ax13.axis('off')
ax13.imshow(img_s_H_mt,cmap='gray',vmax=255,vmin=0)

ax14=plt.subplot(gs1[0,3])
ax14.set_title(f'k=0.00025 (Low Turbulence)')
ax14.axis('off')
ax14.imshow(img_s_H_lt,cmap='gray',vmax=255,vmin=0)

ax15=plt.subplot(gs1[1,0])
ax15.axis('off')
ax15.imshow(it.gamma(0.1,255)(np.abs(img1_f)),cmap='gray')

ax16=plt.subplot(gs1[1,1])
ax16.axis('off')
ax16.imshow(it.gamma(0.1,255)(np.abs(img_f_H_st)),cmap='gray')

ax17=plt.subplot(gs1[1,2])
ax17.axis('off')
ax17.imshow(it.gamma(0.1,255)(np.abs(img_f_H_mt)),cmap='gray')

ax18=plt.subplot(gs1[1,3])
ax18.axis('off')
ax18.imshow(it.gamma(0.1,255)(np.abs(img_f_H_lt)),cmap='gray')

fig1.tight_layout(pad=2.5)
fig1.set_size_inches(13,8)
fig1.suptitle('Visualizing the Atmospheric Turbulence Degradation in an image in the spatial as well as the frequency domain',font='Times New Roman',fontweight="bold",fontsize=16)
fig1.savefig('input_output/C_expt8.jpg',dpi=500)
plt.show()
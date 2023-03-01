'''
C_expt No. 9: 

Title: Visualizing the Motion Blur Degradation in an image in the spatial as well as the frequency domain

Aim: To write a program using Python to visualize the effect of Motion Blur Degradation {H[u,v]=(T/(np.pi*((u-M/2)*a+(v-N/2)*b)))*(np.sin(np.pi*((u-M/2)*a+(v-N/2)*b)))*np.exp(-1j*((u-M/2)*a+(v-N/2)*b))} in the spatial and frequency Domain for:
a=0.1, b=0, T=1
a=0, b=0.1, T=1
a=0.1, b=0.1, T=1
'''

# important imports:
import numpy as np
from matplotlib import pyplot as plt,gridspec as gs

### adding path to dip_toolbox
import sys
sys.path.append('./')

from dip_toolbox import FrequencyDomain,DegradationModels,IntensityTransformations

# creating objects from the classes imported:
fd=FrequencyDomain()
dm=DegradationModels()
it=IntensityTransformations()

# importing the original image:
img1=plt.imread('CH05\Fig0526(a)(original_DIP).tif')
img1_f=fd.dftshift2(fd.dft2(img1))

# motion degradation:
T=1                                               # Motion Time
H_x=dm.motion_blur(img1.shape,a=0.1,b=0,T=T)      # Motion in only x-direction 
H_y=dm.motion_blur(img1.shape,a=0,b=0.1,T=T)      # Motion in only y-direction
H_xy=dm.motion_blur(img1.shape,a=0.1,b=0.1,T=T)   # Motion in both x and y directions

# degraded images in frequency domain:
img_f_H_x=img1_f*H_x
img_f_H_y=img1_f*H_y
img_f_H_xy=img1_f*H_xy

# degraded images in spatial domain:
img_s_H_x=np.real(fd.idft2(fd.dftshift2(img_f_H_x)))
img_s_H_y=np.real(fd.idft2(fd.dftshift2(img_f_H_y)))
img_s_H_xy=np.real(fd.idft2(fd.dftshift2(img_f_H_xy)))


# plots
fig1=plt.figure(1)
gs1=gs.GridSpec(2,4)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[0,1])
ax12.set_title(f'Motion in only x-direction')
ax12.axis('off')
ax12.imshow(img_s_H_x,cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[0,2])
ax13.set_title(f'Motion in only y-direction')
ax13.axis('off')
ax13.imshow(img_s_H_y,cmap='gray',vmax=255,vmin=0)


ax14=plt.subplot(gs1[0,3])
ax14.set_title(f'Motion in both x and y directions')
ax14.axis('off')
ax14.imshow(img_s_H_xy,cmap='gray',vmax=255,vmin=0)

ax15=plt.subplot(gs1[1,0])
ax15.axis('off')
ax15.imshow(it.gamma(0.1,255,np.max(np.abs(img1_f)))(np.abs(img1_f)),cmap='gray')

ax16=plt.subplot(gs1[1,1])
ax16.axis('off')
ax16.set_title(f'a=0.1, b=0, T=1')
ax16.imshow(it.gamma(0.1,255,np.max(np.abs(img_f_H_x)))(np.abs(img_f_H_x)),cmap='gray')

ax17=plt.subplot(gs1[1,2])
ax17.axis('off')
ax17.set_title(f'a=0, b=0.1, T=1')
ax17.imshow(it.gamma(0.1,255,np.max(np.abs(img_f_H_y)))(np.abs(img_f_H_y)),cmap='gray')

ax18=plt.subplot(gs1[1,3])
ax18.axis('off')
ax18.set_title(f'a=0.1, b=0.1, T=1')
ax18.imshow(it.gamma(0.1,255,np.max(np.abs(img_f_H_xy)))(np.abs(img_f_H_xy)),cmap='gray')

fig1.tight_layout(pad=2.5)
fig1.set_size_inches(13,8)
fig1.suptitle('Visualizing the Motion Blur Degradation in an image in the spatial as well as the frequency domain',font='Times New Roman',fontweight="bold",fontsize=16)
fig1.savefig('input_output/C_expt9.jpg',dpi=500)
plt.show()
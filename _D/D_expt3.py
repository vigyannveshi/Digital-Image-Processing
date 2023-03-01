'''

D_expt No. 3: 

Title: Visualizing the importance of Fourier Spectrum and phase angle

Aim: To write a program using Python to visualize the importance of Fourier Spectrum and phase angle

'''

# important imports:
import numpy as np
import matplotlib.pyplot as plt

# appending path to dip_toolbox
import sys
sys.path.append('./')

from dip_toolbox import FrequencyDomain,PlottingFunctions,IntensityTransformations,Filters

# creating objects from classes:
fd=FrequencyDomain()
pf=PlottingFunctions()
it=IntensityTransformations()
flt=Filters()

# importing images:
img1=plt.imread('CH04\Fig0424(a)(rectangle).tif')
img2=plt.imread('CH04\Fig0427(a)(woman).tif')

# cropping excess of img1 from its edges:
img1=fd.unpad_img(img1,up_c=512,up_r=512,center=True)

# DFT of images:
img1_f=fd.dft2(img1*fd.freq_trans(img1.shape))
img2_f=fd.dft2(img2*fd.freq_trans(img2.shape))

# Fourier spectrum and phase angle of images
img1_sp,img1_pa=np.abs(img1_f),np.angle(img1_f)
img2_sp,img2_pa=np.abs(img2_f),np.angle(img2_f)


# unit magnitude spectrum 
ums=lambda img_shape:np.ones(img_shape)

# Re-assigning phase and spectrum:

### unit magnitude spectrum + phase of img1
u_img1p=fd.cps(ums(img1_sp.shape),img1_pa)

### unit magnitude spectrum + phase of img2
u_img2p=fd.cps(ums(img2_sp.shape),img2_pa)

### spectrum of img2 + phase of img 1
sp2_img1p=fd.cps(img2_sp,img1_pa)

### spectrum of img1 + phase of img 2
sp1_img2p=fd.cps(img1_sp,img2_pa)


# plotting:

### figure 1
fig_1_imgs=[img1,it.gamma(0.2,255)(img1_sp/fd.prod_rc(img1.shape)),flt.isc(img1_pa,100),img2,it.gamma(0.2,255)(img2_sp/fd.prod_rc(img2.shape)),flt.isc(img2_pa,100)]

fig_1_titles=["img1", "|IMG1|",r"$\angle$IMG1", "img2", "|IMG2|",r"$\angle$IMG2"]

fig_1_ttl="Spectrum and Phase of Image 1 and 2"

fig_1_save_ttl="D_expt3_1.jpg"

pf.plot(fig_1_imgs,fig_1_titles,1,(2,3),fig_1_ttl,fig_1_save_ttl,fig_pad=2.4)


### figure 2

imgs_list=[u_img1p,u_img2p,sp2_img1p,sp1_img2p]
fig_2_imgs=[]

#### converting the images into spatial domain and appending them in list of fig_2_imgs
for i in imgs_list:
    fig_2_imgs.append(np.real(fd.idft2(i))*fd.freq_trans(i.shape))

fig_2_imgs[0]=flt.isc(fig_2_imgs[0],150)
fig_2_imgs[1]=(flt.isc(fig_2_imgs[1],200)) 

fig_2_titles=[r"$\angle$IMG1 +|1|", r"$\angle$IMG2 +|1|",r"$\angle$IMG1 + |IMG2|", r"$\angle$IMG2 + |IMG1|"]

fig_2_ttl="Visualising importance of Fourier Spectrum and phase angle (Spatial Domain Output)"

fig_2_save_ttl="D_expt3_2.jpg"

pf.plot(fig_2_imgs,fig_2_titles,2,(2,2),fig_2_ttl,fig_2_save_ttl,fig_pad=1.5)

# displaying plots:
pf.show()
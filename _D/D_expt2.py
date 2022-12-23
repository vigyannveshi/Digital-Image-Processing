'''

D_expt No. 2: 

Title: Visualizing the effect of Translation and Rotation in spatial domain and its corresponding frequency spectrum

Aim: To write a program using Python to visualize the effect of Translation and Rotation in spatial domain and its corresponding frequency spectrum

'''

# important imports
from matplotlib import pyplot as plt
import numpy as np

### adding path to dip_toolbox
import sys
sys.path.append('./')

from dip_toolbox import FrequencyDomain, GeometricTransforms, PlottingFunctions

# objects from the imported class:
gt=GeometricTransforms()
fd=FrequencyDomain()
pf=PlottingFunctions()

img1=plt.imread('CH04\Fig0424(a)(rectangle).tif')
img1_pd=fd.pad_img(img1)
img_f=fd.dft2(img1_pd*fd.freq_trans(img1_pd.shape))
imf_r=np.real(img_f)
imf_i=np.imag(img_f)


# Geometric Transformation in spatial domain:
angle=60
tx=300
ty=-300

sg_img_r=gt.tf(img1,gt.rt(gt.cen(img1),angle))
sg_img_t=gt.tf(img1,gt.tr(tx,ty))
sg_img_tr=gt.tf(gt.tf(img1,gt.rt(gt.cen(img1),angle)),gt.tr(tx,ty))
f_img_r=fd.dft2(sg_img_r*fd.freq_trans(sg_img_r.shape))
f_img_t=fd.dft2(sg_img_t*fd.freq_trans(sg_img_t.shape))
f_img_tr=fd.dft2(sg_img_tr*fd.freq_trans(sg_img_tr.shape))


# plotting:

### Figure 1:

fig_1_imgs=[img1,sg_img_r,sg_img_t,sg_img_tr,np.abs(img_f),np.abs(f_img_r),np.abs(f_img_t),np.abs(f_img_tr)]

fig_1_titles=["Original Image", f"Rotated by {angle}°",f"Translated by tx={tx}, ty={ty}", f"Trans({tx,ty}) + Rot({angle})","","","",""]

fig_1_ttl="Translation and Rotation in spatial domain and its corresponding frequency spectrum "

fig_1_save_ttl="D_expt2_1.jpg"

pf.plot(fig_1_imgs,fig_1_titles,1,(2,4),fig_1_ttl,fig_1_save_ttl,fig_pad=2.2)

plt.show()

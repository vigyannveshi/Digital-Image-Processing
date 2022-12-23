'''
B_expt No. 1f: 

Gamma Transformations

Note: By default matplotlib.pyplot stretches the contrast of the image, which is not expected by us as learners, so we need to pass the lower and higher values of intensities in imshow(img,vmin=0,vmax=255) to get output as per our transform function

'''

# important imports
import numpy as np
from matplotlib import pyplot as plt, gridspec as gs

### adding path to dip_toolbox
import sys
sys.path.append('./')

from dip_toolbox import IntensityTransformations

# initializing object from IntensityTransformations class
it=IntensityTransformations()

# importing images
img1=plt.imread('CH03\Fig0308(a)(fractured_spine).tif')
img2=plt.imread('CH03\Fig0309(a)(washed_out_aerial_image).tif')

# intensity levels
L=256

# gm_1 Transformations
r=np.arange(0,L)
gm_1=[2,0.6,0.4,0.3]
s1=[]
img_o_1=[]
for p in gm_1:
    s1.append(it.gamma(p,L)(r))
    img_o_1.append(it.gamma(p,L)(img1))
    
# gm_2 Transformations
r=np.arange(0,L)
gm_2=[0.2,3.0,4.0,5.0]
s2=[]
img_o_2=[]
for p in gm_2:
    s2.append(it.gamma(p,L)(r))
    img_o_2.append(it.gamma(p,L)(img2))



# plotting:
fig1=plt.figure(1)
gs1=gs.GridSpec(2,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmin=0,vmax=255)


ax12=plt.subplot(gs1[1,0])
ax12.set_title('Transformation functions')
ax12.plot(r,s1[0])
ax12.plot(r,s1[1])
ax12.plot(r,s1[2])
ax12.plot(r,s1[3])
ax12.legend(gm_1)
ax12.set_xlabel('input image intensity (r)')
ax12.set_ylabel('output image intensity (s)')

ax13=plt.subplot(gs1[0,1])
ax13.set_title(f'γ = {gm_1[0]}')
ax13.axis('off')
ax13.imshow(img_o_1[0],cmap='gray',vmin=0,vmax=255)

ax14=plt.subplot(gs1[0,2])
ax14.set_title(f'γ ={gm_1[1]}')
ax14.axis('off')
ax14.imshow(img_o_1[1],cmap='gray',vmin=0,vmax=255)

ax15=plt.subplot(gs1[1,1])
ax15.set_title(f'γ = {gm_1[2]}')
ax15.axis('off')
ax15.imshow(img_o_1[2],cmap='gray',vmin=0,vmax=255)

ax16=plt.subplot(gs1[1,2])
ax16.set_title(f'γ = {gm_1[3]}')
ax16.axis('off')
ax16.imshow(img_o_1[3],cmap='gray',vmin=0,vmax=255)

plt.suptitle('Gamma  Transformations ',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
fig1.set_size_inches(13, 8)
plt.savefig('input_output/B_expt1_f_1.jpg',dpi=500)


fig2=plt.figure(2)
gs2=gs.GridSpec(2,3)

ax21=plt.subplot(gs2[0,0])
ax21.set_title('Original image')
ax21.axis('off')
ax21.imshow(img2,cmap='gray',vmin=0,vmax=255)


ax22=plt.subplot(gs2[1,0])
ax22.set_title('Transformation functions')
ax22.plot(r,s2[0])
ax22.plot(r,s2[1])
ax22.plot(r,s2[2])
ax22.plot(r,s2[3])
ax22.legend(gm_2)
ax22.set_xlabel('input image intensity (r)')
ax22.set_ylabel('output image intensity (s)')

ax23=plt.subplot(gs2[0,1])
ax23.set_title(f'γ = {gm_2[0]}')
ax23.axis('off')
ax23.imshow(img_o_2[0],cmap='gray',vmin=0,vmax=255)

ax24=plt.subplot(gs2[0,2])
ax24.set_title(f'γ ={gm_2[1]}')
ax24.axis('off')
ax24.imshow(img_o_2[1],cmap='gray',vmin=0,vmax=255)

ax25=plt.subplot(gs2[1,1])
ax25.set_title(f'γ = {gm_2[2]}')
ax25.axis('off')
ax25.imshow(img_o_2[2],cmap='gray',vmin=0,vmax=255)

ax26=plt.subplot(gs2[1,2])
ax26.set_title(f'γ = {gm_2[3]}')
ax26.axis('off')
ax26.imshow(img_o_2[3],cmap='gray',vmin=0,vmax=255)

plt.suptitle('Gamma  Transformations ',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
fig2.set_size_inches(13, 8)
plt.savefig('input_output/B_expt1_f_2.jpg',dpi=500)
plt.show()

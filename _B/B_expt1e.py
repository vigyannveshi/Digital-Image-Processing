'''
B_expt No. 1e: 

Logarithmic and Antilogarithmic Transformations

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
img1=plt.imread('CH03\Fig0305(a)(DFT_no_log).tif')

# intensity levels
L=256

r1=np.arange(0,np.max(img1))
# Logarithmic Transformation
s1,img2=it.log(L,np.max(r1))(r1),it.log(L,np.max(img1))(img1)

r2=np.arange(0,np.max(img2))
# Antilogarithmic Transformation
s2,img3=it.antilog(L,np.max(r2))(r2),it.antilog(L,np.max(img2))(img2)


# plotting:
fig1=plt.figure(1)
gs1=gs.GridSpec(2,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmin=0,vmax=255)


ax12=plt.subplot(gs1[0,1])
ax12.set_title('Transformation function')
ax12.plot(r1,s1)
ax12.set_xlabel('input image intensity (r)')
ax12.set_ylabel('output image intensity (s)')

ax13=plt.subplot(gs1[0,2])
ax13.set_title('Logarithmically transformed image')
ax13.axis('off')
ax13.imshow(img2,cmap='gray',vmin=0,vmax=255)


ax13=plt.subplot(gs1[1,0])
ax13.set_title('Logarithmically transformed image')
ax13.axis('off')
ax13.imshow(img2,cmap='gray',vmin=0,vmax=255)


ax12=plt.subplot(gs1[1,1])
ax12.set_title('Transformation function')
ax12.plot(r2,s2)
ax12.set_xlabel('input image intensity (r)')
ax12.set_ylabel('output image intensity (s)')

ax13=plt.subplot(gs1[1,2])
ax13.set_title('Antilogarithmically transformed image')
ax13.axis('off')
ax13.imshow(img3,cmap='gray',vmin=0,vmax=255)

plt.suptitle('Logarithmic and Antilogarithmic  Transformation ',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=1)
fig1.set_size_inches(13, 8)
plt.savefig('input_output/B_expt1_e.jpg',dpi=500)
plt.show()

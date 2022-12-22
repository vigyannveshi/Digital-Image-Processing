'''
B_expt No. 1c: 

Intensity level Slicing

Note: By default matplotlib.pyplot stretches the contrast of the image, which is not expected by us as learners, so we need to pass the lower and higher values of intensities in imshow(img,vmin=0,vmax=255)
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
img1=plt.imread('CH03\Fig0312(a)(kidney).tif')

# intensity levels
L=256

r=np.arange(0,L-1)

# Intensity level slicing
a=[150,230]; b=250; s=0

### Thresholded Intensity level slicing:
img2,s1=it.intensity_level_slice(a,0,b,s)(img1),it.intensity_level_slice(a,0,b,s)(r)

### Linear Intensity level slicing
img3,s2=it.intensity_level_slice(a,1,b,s)(img1),it.intensity_level_slice(a,1,b,s)(r)

# plotting:
fig1=plt.figure(1)
gs1=gs.GridSpec(2,3)

ax11=plt.subplot(gs1[0:2,0:1])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmin=0,vmax=255)


ax12=plt.subplot(gs1[0,1])
ax12.set_title('Transformation function')
ax12.plot(r,s1)
ax12.set_xlabel('input image intensity (r)')
ax12.set_ylabel('output image intensity (s)')

ax13=plt.subplot(gs1[0,2:3])
ax13.set_title('Thresholded intensity level sliced image')
ax13.axis('off')
ax13.imshow(img2,cmap='gray',vmin=0,vmax=255)



ax14=plt.subplot(gs1[1,1])
ax14.set_title('Transformation function')
ax14.plot(r,s2)
ax14.set_xlabel('input image intensity (r)')
ax14.set_ylabel('output image intensity (s)')

ax15=plt.subplot(gs1[1,2:3])
ax15.set_title('Linear Intensity level sliced image')
ax15.axis('off')
ax15.imshow(img3,cmap='gray',vmin=0,vmax=255)

plt.suptitle('Intensity level slicing ',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=0.5)
fig1.set_size_inches(13, 8)
plt.savefig('input_output/B_expt1_c.jpg',dpi=500)
plt.show()

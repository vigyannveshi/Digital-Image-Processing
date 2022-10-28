'''
e) Logarithmic and Antilogarithmic Transformations

Note: By default matplotlib.pyplot stretches the contrast of the image, which is not expected by us as learners, so we need to pass the lower and higher values of intensities in imshow(img,vmin=0,vmax=255) to get output as per our transform function

'''

# important imports
import numpy as np
from matplotlib import pyplot as plt, gridspec as gs
from dip_toolbox import IntensityTransformations

# initializing object from IntensityTransformations class
it=IntensityTransformations()

# importing images
img1=plt.imread('CH03\Fig0305(a)(DFT_no_log).tif')

# intensity levels
L=256

r=np.arange(0,L)
# Logarithmic Transformation
s1,img2=it.log(L)(r),it.log(L)(img1)
# Antilogarithmic Transformation
s2,img3=it.antilog(L)(r),it.antilog(L)(img2)


# plotting:
fig1=plt.figure(1)
gs1=gs.GridSpec(2,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmin=0,vmax=255)


ax12=plt.subplot(gs1[0,1])
ax12.set_title('Transformation function')
ax12.plot(r,s1)
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
ax12.plot(r,s2)
ax12.set_xlabel('input image intensity (r)')
ax12.set_ylabel('output image intensity (s)')

ax13=plt.subplot(gs1[1,2])
ax13.set_title('Antilogarithmically transformed image')
ax13.axis('off')
ax13.imshow(img3,cmap='gray',vmin=0,vmax=255)

plt.suptitle('Logarithmic and Antilogarithmic  Transformation ',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=1)
fig1.set_size_inches(13, 8)
plt.savefig('input_output/expt8_e.jpg',dpi=500)
plt.show()

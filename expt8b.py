'''
b) Thresholding

Note: By default matplotlib.pyplot stretches the contrast of the image, which is not expected by us as learners, so we need to pass the lower and higher values of intensities in imshow(img,vmin=0,vmax=255)
'''

# important imports
import numpy as np
from matplotlib import pyplot as plt, gridspec as gs
from dip_toolbox import IntensityTransformations

# initializing object from IntensityTransformations class
it=IntensityTransformations()

# importing images
img1=plt.imread('CH03\Fig0310(b)(washed_out_pollen_image).tif')

# intensity levels
L=256

# thresholding done at mean intensity level
m=np.int64(np.mean(img1))

thr=it.threshold(m,L)
r=np.arange(0,L)
s,img2=thr(r),thr(img1)


# plotting:
fig1=plt.figure(1)
gs1=gs.GridSpec(1,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmin=0,vmax=255)


ax12=plt.subplot(gs1[0,1])
ax12.set_title('Transformation function')
ax12.plot(r,s)
ax12.set_xlabel('input image intensity (r)')
ax12.set_ylabel('output image intensity (s)')

ax13=plt.subplot(gs1[0,2])
ax13.set_title('Thresholded image')
ax13.axis('off')
ax13.imshow(img2,cmap='gray',vmin=0,vmax=255)

plt.suptitle('Thresholding at mean intensity level',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=2.5)
fig1.set_size_inches(13, 8)
plt.savefig('input_output/expt8_b.jpg',dpi=500)
plt.show()

'''
C_expt No. 4a: 

Title: Handling Salt & Pepper, Gaussian and Uniform noise using Order Statistic filters

Aim: To write a program using Python to add  salt and  pepper noise to  an original image, then apply filters and check their performance
a) Repeated use of Median filter
b) Using Max, Min, Midpoint filters 

'''

# important imports:
from matplotlib import pyplot as plt,gridspec as gs

### adding path to dip_toolbox
import sys
sys.path.append('./')

from dip_toolbox import NoiseModels, Filters

# creating objects from NoiseModels and Filters class:
nm=NoiseModels()
flt=Filters()

# importing original image:
img1=plt.imread('CH05\Fig0507(a)(ckt-board-orig).tif')

# adding Salt and Pepper Noise with probabilities Ps=Pp=0.1:
spn_img=nm.salt_pepper_noise(img1,0.1,0.1)

# i) Applying Median filters of order 3*3 repeatedly:
flt_img_1=flt.flt_apply(img1,3,flt.median_flt)
flt_img_2=flt.flt_apply(flt_img_1,3,flt.median_flt)
flt_img_3=flt.flt_apply(flt_img_2,3,flt.median_flt)
flt_img_4=flt.flt_apply(flt_img_3,3,flt.median_flt)


# plots:

fig1=plt.figure(1)
gs1=gs.GridSpec(2,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[0,1])
ax12.set_title(f'Image with S&P (Ps=Pp=0.1)')
ax12.axis('off')
ax12.imshow(spn_img,cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[0,2])
ax13.set_title(f'Median Filtered (1)')
ax13.axis('off')
ax13.imshow(flt_img_1,cmap='gray',vmax=255,vmin=0)

ax14=plt.subplot(gs1[1,0])
ax14.set_title(f'Median Filtered (2)')
ax14.axis('off')
ax14.imshow(flt_img_2,cmap='gray',vmax=255,vmin=0)

ax15=plt.subplot(gs1[1,1])
ax15.set_title(f'Median Filtered (3)')
ax15.axis('off')
ax15.imshow(flt_img_3,cmap='gray',vmax=255,vmin=0)

ax16=plt.subplot(gs1[1,2])
ax16.set_title(f'Median Filtered (4)')
ax16.axis('off')
ax16.imshow(flt_img_4,cmap='gray',vmax=255,vmin=0)

fig1.tight_layout(pad=3)
fig1.set_size_inches(13,8)
fig1.suptitle('Handling Salt & Pepper noise using Order Statistic filters: a) Repeat (3*3) Median filter ',font='Times New Roman',fontweight="bold",fontsize=16)
fig1.savefig('input_output/C_expt4_a.jpg',dpi=500)

plt.show()


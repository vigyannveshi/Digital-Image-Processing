'''
B_expt No. 1g: 

Bit-plane slicing 

Note: By default matplotlib.pyplot stretches the contrast of the image, which is not expected by us as learners, so we need to pass the lower and higher values of intensities in imshow(img,vmin=0,vmax=255) to get output as per our transform function

'''

# important imports
from matplotlib import pyplot as plt, gridspec as gs
from dip_toolbox import IntensityTransformations

# initializing object from IntensityTransformations class
it=IntensityTransformations()

# importing images
img1=plt.imread('CH03\Fig0314(a)(100-dollars).tif')

# Bitplane slicing
img_bp_1=it.bit_plane_slicing(img1)


# plotting:
fig1=plt.figure(1)
gs1=gs.GridSpec(3,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmin=0,vmax=255)

ax12=plt.subplot(gs1[0,1])
ax12.set_title('Bitplane: 0')
ax12.axis('off')
ax12.imshow(img_bp_1[0],cmap='gray',vmin=0,vmax=255)

ax13=plt.subplot(gs1[0,2])
ax13.set_title('Bitplane: 1')
ax13.axis('off')
ax13.imshow(img_bp_1[1],cmap='gray',vmin=0,vmax=255)

ax14=plt.subplot(gs1[1,0])
ax14.set_title('Bitplane: 2')
ax14.axis('off')
ax14.imshow(img_bp_1[2],cmap='gray',vmin=0,vmax=255)

ax15=plt.subplot(gs1[1,1])
ax15.set_title('Bitplane: 3')
ax15.axis('off')
ax15.imshow(img_bp_1[3],cmap='gray',vmin=0,vmax=255)

ax16=plt.subplot(gs1[1,2])
ax16.set_title('Bitplane: 4')
ax16.axis('off')
ax16.imshow(img_bp_1[4],cmap='gray',vmin=0,vmax=255)

ax17=plt.subplot(gs1[2,0])
ax17.set_title('Bitplane: 5')
ax17.axis('off')
ax17.imshow(img_bp_1[5],cmap='gray',vmin=0,vmax=255)

ax18=plt.subplot(gs1[2,1])
ax18.set_title('Bitplane: 6')
ax18.axis('off')
ax18.imshow(img_bp_1[6],cmap='gray',vmin=0,vmax=255)

ax18=plt.subplot(gs1[2,2])
ax18.set_title('Bitplane: 7')
ax18.axis('off')
ax18.imshow(img_bp_1[7],cmap='gray',vmin=0,vmax=255)

plt.suptitle('Bit plane slicing ',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=3)
fig1.set_size_inches(13, 8)
plt.savefig('input_output/B_expt1_g_1.jpg',dpi=500)
plt.show()



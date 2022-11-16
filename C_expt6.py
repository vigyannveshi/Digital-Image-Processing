'''
C_expt No. 6: 

Title: Handling Salt & Pepper Noise with probabilities Ps>0.2, Pp>0.2 using Adaptive Median Filter

Aim: To write a program using Python to add  salt and  pepper noise to an original image with higher probabilities, and appreciate the filtering difference between median and adaptive median filter. 

'''

# important imports:
from matplotlib import pyplot as plt,gridspec as gs
from dip_toolbox import NoiseModels, Filters

# creating objects from NoiseModels and Filters class:
nm=NoiseModels()
flt=Filters()

# importing original image:
img1=plt.imread('CH05\Fig0507(a)(ckt-board-orig).tif')

# adding Salt and Pepper Noise with probabilities Ps=Pp=0.25:
spn_img=nm.salt_pepper_noise(img1,0.25,0.25)

# filtering using 7*7 Median Filter, Adaptive Median Filter (Smax=7):
flt_md_img=flt.flt_apply(spn_img,7,flt.median_flt,pad_with=255)
flt_amd_img=flt.adpt_median_flt(spn_img,7,pad_with=255)

# plots:
fig1=plt.figure(1)
gs1=gs.GridSpec(2,2)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[0,1])
ax12.set_title(f'img + sp(pp=ps=0.25)')
ax12.axis('off')
ax12.imshow(spn_img,cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[1,0])
ax13.set_title(f'Filtered using Median Flt (7*7)')
ax13.axis('off')
ax13.imshow(flt_md_img,cmap='gray',vmax=255,vmin=0)

ax14=plt.subplot(gs1[1,1])
ax14.set_title(f'Filtered using Adpt Median Flt (Smax=7)')
ax14.axis('off')
ax14.imshow(flt_amd_img,cmap='gray',vmax=255,vmin=0)

fig1.tight_layout(pad=1.5)
fig1.set_size_inches(13,8)
fig1.suptitle('Handling Salt & Pepper Noise with probabilities Ps>0.2, Pp>0.2 using Adaptive Median Filter',font='Times New Roman',fontweight="bold",fontsize=16)
fig1.savefig('input_output/C_expt6.jpg',dpi=500)
plt.show()
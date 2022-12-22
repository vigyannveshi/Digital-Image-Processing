'''
C_expt No. 2: 

Title: Noise removal using various mean filters

Aim: To write a program using Python to add gaussian noise to  an original image, then apply mean filters and check their performance
i)    Arithmetic mean filter (3*3)
ii)   Geometric mean filter (3*3)
iii)  Harmonic mean filter (3*3)
iv)   Contraharmonic mean filter (3*3), q=2
v)    Arithmetic mean filter (5*5)
vi)   Geometric mean filter (5*5)
vii)  Harmonic mean filter (5*5)
viii) Contraharmonic mean filter (5*5), q=2

'''

# important imports
from matplotlib import pyplot as plt, gridspec as gs

### adding path to dip_toolbox
import sys
sys.path.append('./')

from dip_toolbox import NoiseModels, Filters

# importing image and addition of Gaussian noise:
img1=plt.imread('CH05\Fig0507(a)(ckt-board-orig).tif')

nm=NoiseModels()
mean=0;var=500
gn=nm.gaussian_noise(img1.shape,0,500)
gn_img=nm.add_noise(gn,img1)


# creating object from Filters class
imf=Filters()


# plots
fig1=plt.figure(1)
gs1=gs.GridSpec(2,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[0,1])
ax12.set_title(f'AGN: $\mu$={mean}, $\sigma^2$={var}')
ax12.axis('off')
ax12.imshow(gn_img,cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[0,2])
ax13.set_title(f'AM filter (3*3) ')
ax13.axis('off')
ax13.imshow(imf.flt_apply(gn_img,3,imf.am_flt,pad_with=255),cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[1,0])
ax13.set_title(f'GM filter (3*3) ')
ax13.axis('off')
ax13.imshow(imf.flt_apply(gn_img,3,imf.gm_flt,pad_with=255),cmap='gray',vmax=255,vmin=0)

ax14=plt.subplot(gs1[1,1])
ax14.set_title(f'HM filter (3*3) ')
ax14.axis('off')
ax14.imshow(imf.flt_apply(gn_img,3,imf.hm_flt,pad_with=255),cmap='gray',vmax=255,vmin=0)

ax15=plt.subplot(gs1[1,2])
ax15.set_title(f'CHM filter(q=2) (3*3) ')
ax15.axis('off')
ax15.imshow(imf.flt_apply(gn_img,3,imf.chm_flt(2),pad_with=255),cmap='gray',vmax=255,vmin=0)


fig1.tight_layout(pad=2.5)
fig1.set_size_inches(13,8)
fig1.suptitle('Noise removal using various mean filters (3*3) ',font='Times New Roman',fontweight="bold",fontsize=16)
fig1.savefig('input_output/C_expt2_1.jpg',dpi=500)

fig2=plt.figure(2)
gs2=gs.GridSpec(2,3)

ax21=plt.subplot(gs2[0,0])
ax21.set_title('Original image')
ax21.axis('off')
ax21.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax22=plt.subplot(gs2[0,1])
ax22.set_title(f'AGN: $\mu$={mean}, $\sigma^2$={var}')
ax22.axis('off')
ax22.imshow(gn_img,cmap='gray',vmax=255,vmin=0)

ax23=plt.subplot(gs2[0,2])
ax23.set_title(f'AM filter (5*5) ')
ax23.axis('off')
ax23.imshow(imf.flt_apply(gn_img,5,imf.am_flt,pad_with=255),cmap='gray',vmax=255,vmin=0)

ax23=plt.subplot(gs2[1,0])
ax23.set_title(f'GM filter (5*5) ')
ax23.axis('off')
ax23.imshow(imf.flt_apply(gn_img,5,imf.gm_flt,pad_with=255),cmap='gray',vmax=255,vmin=0)

ax24=plt.subplot(gs2[1,1])
ax24.set_title(f'HM filter (5*5) ')
ax24.axis('off')
ax24.imshow(imf.flt_apply(gn_img,5,imf.hm_flt,pad_with=255),cmap='gray',vmax=255,vmin=0)

ax25=plt.subplot(gs2[1,2])
ax25.set_title(f'CHM filter(q=2) (5*5) ')
ax25.axis('off')
ax25.imshow(imf.flt_apply(gn_img,5,imf.chm_flt(2),pad_with=255),cmap='gray',vmax=255,vmin=0)


fig2.tight_layout(pad=2.5)
fig2.set_size_inches(13,8)
fig2.suptitle('Noise removal using various mean filters (5*5) ',font='Times New Roman',fontweight="bold",fontsize=16)
fig2.savefig('input_output/C_expt2_2.jpg',dpi=500)
plt.show()
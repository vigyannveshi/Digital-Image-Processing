'''
C_expt No. 4b: 

Using 3*3  Max, Min, Midpoint filters 

'''


# important imports:
from matplotlib import pyplot as plt,gridspec as gs
from dip_toolbox import NoiseModels, Filters

# creating objects from NoiseModels and Filters class:
nm=NoiseModels()
flt=Filters()

# importing original image:
img1=plt.imread('CH05\Fig0507(a)(ckt-board-orig).tif')

# adding noise to original image:

### salt noise with Ps=0.1
sn_img=nm.salt_pepper_noise(img1,0,0.1)
### pepper noise with Ps=0.1
pn_img=nm.salt_pepper_noise(img1,0.1,0)
### salt and pepper noise with Pp=Ps=0.1
spn_img=nm.salt_pepper_noise(img1,0.1,0.1)

### guassian noise with mean:5 and variance:1000
gn=nm.gaussian_noise(img1.shape,5,1000)
img_gn=nm.add_noise(gn,img1)

### uniform noise with a=-50,b=50
un=nm.uniform_noise(img1.shape,-50,50)
img_un=nm.add_noise(un,img1)

# Filtering using Max and Min filter:

### salt noise using min filter
flt_s_mn_img=flt.flt_apply(sn_img,3,flt.min_flt)
### pepper noise using max filter
flt_p_mx_img=flt.flt_apply(pn_img,3,flt.max_flt)
### salt and pepper noise using min filter
flt_sp_mn_img=flt.flt_apply(spn_img,3,flt.min_flt)
### salt and pepper noise using max filter
flt_sp_mx_img=flt.flt_apply(spn_img,3,flt.max_flt)


# Filtering using Midpoint filter:

### guassian noise using midpoint filter
flt_g_mp_img=flt.flt_apply(img_gn,3,flt.midpt_flt)
### uniform noise using midpoint filter
flt_u_mp_img=flt.flt_apply(img_un,3,flt.midpt_flt)
### salt and pepper noise using midpoint filter
flt_sp_mp_img=flt.flt_apply(spn_img,3,flt.midpt_flt)


# plots

### Filtering using Max and Min filter:

fig1=plt.figure(1)
gs1=gs.GridSpec(2,4)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[0,1])
ax12.set_title(f'Salt Noise (Ps=0.1)')
ax12.axis('off')
ax12.imshow(sn_img,cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[0,2])
ax13.set_title(f'Pepper Noise (Pp=0.1)')
ax13.axis('off')
ax13.imshow(pn_img,cmap='gray',vmax=255,vmin=0)


ax14=plt.subplot(gs1[0,3])
ax14.set_title(f'Salt & Pepper Noise (Pp=Pp=0.1) ')
ax14.axis('off')
ax14.imshow(spn_img,cmap='gray',vmax=255,vmin=0)

ax15=plt.subplot(gs1[1,0])
ax15.set_title(f'SN using Min flt ')
ax15.axis('off')
ax15.imshow(flt_s_mn_img,cmap='gray',vmax=255,vmin=0)

ax16=plt.subplot(gs1[1,1])
ax16.set_title(f'PN using Max flt')
ax16.axis('off')
ax16.imshow(flt_p_mx_img,cmap='gray',vmax=255,vmin=0)

ax17=plt.subplot(gs1[1,2])
ax17.set_title(f'SPN using Min flt')
ax17.axis('off')
ax17.imshow(flt_sp_mn_img,cmap='gray',vmax=255,vmin=0)

ax18=plt.subplot(gs1[1,3])
ax18.set_title(f'SPN using Max flt')
ax18.axis('off')
ax18.imshow(flt_sp_mx_img,cmap='gray',vmax=255,vmin=0)

fig1.tight_layout(pad=2.5)
fig1.set_size_inches(13,8)
fig1.suptitle('Handling Salt & Pepper noise using Order Statistic filters: 1) Using 3*3 Max and Min filters ',font='Times New Roman',fontweight="bold",fontsize=16)
fig1.savefig('input_output/C_expt4b_1.jpg',dpi=500)


# Filtering using Midpoint Filters

fig2=plt.figure(2)
gs2=gs.GridSpec(2,3)

ax21=plt.subplot(gs2[0,0])
ax21.set_title('Original image')
ax21.axis('off')
ax21.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax22=plt.subplot(gs2[0,1])
ax22.set_title(f'Image with GN ($\mu$=5, $\sigma^2$=1000)')
ax22.axis('off')
ax22.imshow(img_gn,cmap='gray',vmax=255,vmin=0)

ax23=plt.subplot(gs2[0,2])
ax23.set_title(f'Image with UN (a=-50, b=50)')
ax23.axis('off')
ax23.imshow(img_un,cmap='gray',vmax=255,vmin=0)

ax24=plt.subplot(gs2[1,0])
ax24.set_title(f'SPN with Midpoint Flt')
ax24.axis('off')
ax24.imshow(flt_sp_mp_img,cmap='gray',vmax=255,vmin=0)

ax25=plt.subplot(gs2[1,1])
ax25.set_title(f'GN with Midpoint Flt')
ax25.axis('off')
ax25.imshow(flt_g_mp_img,cmap='gray',vmax=255,vmin=0)

ax26=plt.subplot(gs2[1,2])
ax26.set_title(f'UN with Midpoint Flt')
ax26.axis('off')
ax26.imshow(flt_u_mp_img,cmap='gray',vmax=255,vmin=0)

fig2.tight_layout(pad=3)
fig2.set_size_inches(13,8)
fig2.suptitle('Handling Salt & Pepper, Gaussian and Uniform noise using Order Statistic filters: 2) Using 3*3 Mid point filters ',font='Times New Roman',fontweight="bold",fontsize=16)
fig2.savefig('input_output/C_expt4b_2.jpg',dpi=500)

plt.show()

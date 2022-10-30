'''
C_expt No. 1: 

Title: Image Noise Analysis in Digital Image Processing using Python

Aim: To write a program using Python to add different types of noise to original image and analyse using histogram:
Noises added: Gaussian, Rayleigh, Gamma/Erlang, Exponential, Uniform, Salt&Pepper

'''

# important imports:
from matplotlib import pyplot as plt,gridspec as gs
from dip_toolbox import NoiseModels

# importing original image
img1=plt.imread('CH05\Fig0503 (original_pattern).tif')
size=img1.shape
img2=plt.imread('CH05\Fig0504(c)(gamma-noise).tif')

# Creating noise models and adding noise to original image:
nm=NoiseModels()

gn=nm.gaussian_noise(size,5,200)
rn=nm.rayleigh_noise(size,5,20)
en=nm.erlang_noise(size,0.1,2)
xn=nm.exponential_noise(size,0.1)
un=nm.uniform_noise(size,-10,10)

img_gn=nm.add_noise(gn,img1)
img_rn=nm.add_noise(rn,img1)
img_en=nm.add_noise(en,img1)
img_xn=nm.add_noise(xn,img1)
img_un=nm.add_noise(un,img1)
img_sp=nm.salt_pepper_noise(img1,pp=0.2,ps=0.2)


# plots

fig1=plt.figure(1)
gs1=gs.GridSpec(2,4)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original Image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[1,0])
ax12.hist(img1.ravel(),bins=256,density=True,ec='b')
ax12.set_title('Original')


ax13=plt.subplot(gs1[0,1])
ax13.set_title('AGN, µ=5, $σ^2$=200 ')
ax13.axis('off')
ax13.imshow(img_gn,cmap='gray',vmax=255,vmin=0)

ax14=plt.subplot(gs1[1,1])
ax14.hist(img_gn.ravel(),bins=256,density=True,ec='b')
ax14.set_title('Gaussian')


ax15=plt.subplot(gs1[0,2])
ax15.set_title('ARN, a=5, b=20')
ax15.axis('off')
ax15.imshow(img_rn,cmap='gray',vmax=255,vmin=0)

ax16=plt.subplot(gs1[1,2])
ax16.hist(img_rn.ravel(),bins=256,density=True,ec='b')
ax16.set_title('Rayleigh')


ax17=plt.subplot(gs1[0,3])
ax17.set_title('AEN, a=0.1, b=2')
ax17.axis('off')
ax17.imshow(img_en,cmap='gray',vmax=255,vmin=0)

ax18=plt.subplot(gs1[1,3])
ax18.hist(img_en.ravel(),bins=256,density=True,ec='b')
ax18.set_title('Gamma')

plt.tight_layout(pad=1.1)
fig1.set_size_inches(13,8)
plt.suptitle('Image Noise Analysis ',font='Times New Roman',fontweight="bold",fontsize=16)
plt.savefig('input_output/C_expt1_1.jpg',dpi=500)


fig2=plt.figure(2)
gs2=gs.GridSpec(2,3)

ax21=plt.subplot(gs2[0,0])
ax21.set_title('AXN, a=0.1')
ax21.axis('off')
ax21.imshow(img_xn,cmap='gray',vmax=255,vmin=0)

ax22=plt.subplot(gs2[1,0])
ax22.hist(img_xn.ravel(),bins=256,density=True,ec='b')
ax22.set_title('Exponential')


ax23=plt.subplot(gs2[0,1])
ax23.set_title('AUN, a=-10, b=10 ')
ax23.axis('off')
ax23.imshow(img_un,cmap='gray',vmax=255,vmin=0)

ax24=plt.subplot(gs2[1,1])
ax24.hist(img_un.ravel(),bins=256,density=True,ec='b')
ax24.set_title('Uniform')


ax25=plt.subplot(gs2[0,2])
ax25.set_title('ASPN, pp=0.2, ps=0.2')
ax25.axis('off')
ax25.imshow(img_sp,cmap='gray',vmax=255,vmin=0)

ax26=plt.subplot(gs2[1,2])
ax26.hist(img_sp.ravel(),bins=256,density=True,ec='b')
ax26.set_title('Salt & Pepper')


plt.tight_layout(pad=2.5)
fig2.set_size_inches(13,8)
plt.suptitle('Image Noise Analysis ',font='Times New Roman',fontweight="bold",fontsize=16)
plt.savefig('input_output/C_expt1_2.jpg',dpi=500)
plt.show()
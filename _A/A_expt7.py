'''
A_expt No. 7: 

Title: Geometric Spatial Transformation in Digital Image Processing using Python

Aim: To write a program using Python to perform the following Transformation:
    a) Identity
    b) Scaling 
    c) Rotation
    d) Translation
    e) Sheer (vertical)
    f) Sheer (horizontal)
'''

# important imports
from matplotlib import pyplot as plt,gridspec as gs

### adding path to dip_toolbox
import sys
sys.path.append('./')

from dip_toolbox import GeometricTransforms 

# importing images
img1=plt.imread("CH02\Fig0236(a)(letter_T).tif")

# creating class Geometric Transfroms:
gt=GeometricTransforms()


# a) Identity
id_img=gt.tf(img1,gt.id)


# b) Scaling 
sc_imgz=gt.tf(img1,gt.sc(1.2,1.2))
sc_imgs=gt.tf(img1,gt.sc(0.5,0.5))


# c) Rotation
rt_img=gt.tf(img1,gt.rt(gt.cen(img1),60))


# d) Translation
tr_img=gt.tf(img1,gt.tr(50,-60))


# e) Sheer (vertical)
sv_img=gt.tf(img1,gt.shr(0,-.3))


# f) Sheer (horizontal)
sh_img=gt.tf(img1,gt.shr(0.3,0))

# Combo-operations:
combo_oper_mat=(gt.tr(0,200) @ gt.sc(0.5,0.75)@ gt.shr(0,-1))
combo_img=gt.tf(img1,combo_oper_mat)


# plotting:
fig1=plt.figure(1)
gs1=gs.GridSpec(2,4)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray')

ax12=plt.subplot(gs1[0,1])
ax12.set_title('Identity image')
ax12.axis('off')
ax12.imshow(id_img,cmap='gray')

ax13=plt.subplot(gs1[0,2])
ax13.set_title('Scaled image (zoomed)')
ax13.axis('off')
ax13.imshow(sc_imgz,cmap='gray')

ax14=plt.subplot(gs1[0,3])
ax14.set_title('Scaled image (shrinked)')
ax14.axis('off')
ax14.imshow(sc_imgs,cmap='gray')

ax15=plt.subplot(gs1[1,0])
ax15.set_title('Rotated image (60°)')
ax15.axis('off')
ax15.imshow(rt_img,cmap='gray')

ax16=plt.subplot(gs1[1,1])
ax16.set_title('Translated image (50,-60)')
ax16.axis('off')
ax16.imshow(tr_img,cmap='gray')

ax17=plt.subplot(gs1[1,2])
ax17.set_title('Vertically sheared image (-0.3)')
ax17.axis('off')
ax17.imshow(sv_img,cmap='gray')

ax18=plt.subplot(gs1[1,3])
ax18.set_title('Horizontally sheared image(0.3)')
ax18.axis('off')
ax18.imshow(sh_img,cmap='gray')


plt.suptitle('Geometric Spatial Transformation',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=2.5)
fig1.set_size_inches(13, 8)
plt.savefig('input_output/A_expt7_1.jpg',dpi=500)


fig2=plt.figure(2)
gs2=gs.GridSpec(1,2)

ax21=plt.subplot(gs2[0,0])
ax21.set_title('Original image')
ax21.axis('off')
ax21.imshow(img1,cmap='gray')

ax22=plt.subplot(gs2[0,1])
ax22.set_title('(Tr(0,200), Sc(0.5,0.75), Shr(0,-1))')
ax22.axis('off')
ax22.imshow(combo_img,cmap='gray')

plt.suptitle('Combination of Geometric Spatial transformations on image',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=2.5)
plt.savefig('input_output/A_expt7_2.jpg',dpi=500)
plt.show()
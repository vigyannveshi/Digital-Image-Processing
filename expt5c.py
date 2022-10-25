''' c) Image Subtraction for Angiography ''' 

# Important imports:
from matplotlib import pyplot as plt, gridspec as gs
import numpy as np


# importing images
img1=plt.imread('CH02\Fig0228(a)(angiography_mask_image).tif')
img2=plt.imread('CH02\Fig0228(b)(angiography_live_ image).tif')


# image subtraction
img3=img2-img1

# enhanced image subtraction
r,c =img3.shape
img4=np.zeros(img3.shape)


for i in range(r):
    for j in range(c):
        diff_param=img3[i][j]/255
        if diff_param>=0.05 and diff_param<=0.1: 
            img4[i][j]=diff_param*10
        elif diff_param>0.1 and diff_param<0.82:
            img4[i][j]=100    
        elif diff_param>=.82 and diff_param<=0.99:
            img4[i][j]=diff_param*10
        else:  
            img4[i][j]=75


# plots 
fig3=plt.figure(3)
gs3=gs.GridSpec(1,2)

ax31=plt.subplot(gs3[0,0])
ax31.set_title("Original Image")
ax31.axis("off")
ax31.imshow(img1,cmap='gray')

ax32=plt.subplot(gs3[0,1])
ax32.set_title("Image with contrast medium")
ax32.axis("off")
ax32.imshow(img2,cmap='gray')

plt.suptitle(' Image Subtraction for Angiography ',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=1.2)
fig3.set_size_inches(10, 8)
plt.savefig('input_output/expt5_c_1.jpg',dpi=300,)
fig3.set_size_inches(5, 4)
plt.show()


fig4=plt.figure(4)
gs4=gs.GridSpec(1,2)

ax43=plt.subplot(gs4[0,0])
ax43.set_title("Difference image")
ax43.axis("off")
ax43.imshow(img3,cmap='gray')

ax44=plt.subplot(gs4[0,1])
ax44.set_title(" Enhanced Difference image")
ax44.axis("off")
ax44.imshow(img4,cmap='gray')

plt.suptitle(' Image Subtraction for Angiography ',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=1.2)
fig4.set_size_inches(10, 8)
plt.savefig('input_output/expt5_c_2.jpg',dpi=300,)
fig4.set_size_inches(5, 4)
plt.show()

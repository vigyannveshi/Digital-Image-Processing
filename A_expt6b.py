'''
A_expt No. 6b:  

Local Blurring using Neighbourhood Processing
'''

# Important imports:
from matplotlib import pyplot as plt, gridspec as gs
from dip_toolbox import Filters

img2=plt.imread('CH02\Fig0235(c)(kidney_original).tif')
imf=Filters()


# Plotting:
fig2=plt.figure(2)
gs2=gs.GridSpec(1,2)
ax21=plt.subplot(gs2[0,0])
ax21.set_title("Original Image")
ax21.axis("off")
ax21.imshow(img2,cmap='gray')

ax22=plt.subplot(gs2[0,1])
ax22.set_title("Blurred Image, Mask:15*15")
ax22.axis("off")
ax22.imshow(imf.flt_apply(img2,15,imf.am_flt),cmap='gray')

plt.suptitle('Local Blurring using Neighbourhood Processing',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
fig2.set_size_inches(10, 8)
plt.savefig('input_output/A_expt6_b_1.jpg',dpi=300,)
fig2.set_size_inches(5, 4)


fig3=plt.figure(3)
gs3=gs.GridSpec(1,2)

ax31=plt.subplot(gs3[0,0])
ax31.set_title("Blurred Image, Mask:29*29")
ax31.axis("off")
ax31.imshow(imf.flt_apply(img2,29,imf.am_flt),cmap='gray')

ax32=plt.subplot(gs3[0,1])
ax32.set_title("Blurred Image, Mask:41*41")
ax32.axis("off")
ax32.imshow(imf.flt_apply(img2,41,imf.am_flt),cmap='gray')

plt.suptitle('Local Blurring using Neighbourhood Processing',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
fig3.set_size_inches(10, 8)
plt.savefig('input_output/A_expt6_b_2.jpg',dpi=300,)
fig3.set_size_inches(5, 4)
plt.show()

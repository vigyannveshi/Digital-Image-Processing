'''e) Image Multiplication for 'Region of Interest' (ROI) Operations'''

# Important imports:
from matplotlib import pyplot as plt, gridspec as gs

# importing images
img1=plt.imread('CH02\Fig0230(a)(dental_xray).tif')
img2=plt.imread('CH02\Fig0230(b)(dental_xray_mask).tif')



# plots 
fig4=plt.figure(4)
gs4=gs.GridSpec(2,4)

ax41=plt.subplot(gs4[0:1,0:2])
ax41.set_title("Original Image")
ax41.axis("off")
ax41.imshow(img1,cmap='gray')

ax42=plt.subplot(gs4[1:2,0:2])
ax42.set_title("Region selection")
ax42.axis("off")
ax42.imshow(img2,cmap='gray')

ax42=plt.subplot(gs4[0:2,2:4])
ax42.set_title("Region of interest")
ax42.axis("off")
ax42.imshow(img1*img2,cmap='gray')

plt.suptitle(' Image Multiplication for "Region of Interest" (ROI) Operations',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
fig4.set_size_inches(10, 8)
plt.savefig('input_output/expt5_e.jpg',dpi=400,)
fig4.set_size_inches(5, 4)
plt.show()
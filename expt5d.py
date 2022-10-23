'''d) Image Multiplication for Shading Correction'''

# Important imports:
from matplotlib import pyplot as plt, gridspec as gs

# importing images
img1=plt.imread('CH02\Fig0229(a)(tungsten_filament_shaded).tif')
img2=plt.imread('CH02\Fig0229(b)(tungsten_sensor_shading).tif')


# plots

# plots 
fig4=plt.figure(4)
gs4=gs.GridSpec(2,4)

ax41=plt.subplot(gs4[0:1,0:2])
ax41.set_title("Original Image")
ax41.axis("off")
ax41.imshow(img1,cmap='gray')

ax42=plt.subplot(gs4[1:2,0:2])
ax42.set_title("Corrective image")
ax42.axis("off")
ax42.imshow(img2,cmap='gray')

ax42=plt.subplot(gs4[0:2,2:4])
ax42.set_title("Corrected image")
ax42.axis("off")
ax42.imshow(img1*(1/img2),cmap='gray')

plt.suptitle(' Image Multiplication for Shading Correction ',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
fig4.set_size_inches(10, 8)
plt.savefig('input_output/expt5_d.jpg',dpi=400,)
fig4.set_size_inches(5, 4)
plt.show()
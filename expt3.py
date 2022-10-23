'''
Expt No. 3: 

Title: Image Resolution

Aim: To write a program using Python to visualize typical Effects of Reducing Spatial Resolution

'''

from matplotlib import pyplot as plt, gridspec as gs


''' Creating the images with reduced spatial resolution '''

# img1=plt.imread('CH02\Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif')

# fig1=plt.figure(1,dpi=1250)
# plt.axis('off')
# plt.imshow(img1,cmap='gray',interpolation='none')
# fig1.savefig('input_output\expt3_dpi_1250.jpg',dpi=1250)
# plt.show()

# fig2=plt.figure(2,dpi=300)
# plt.axis('off')
# plt.imshow(img1,cmap='gray',interpolation='none')
# fig2.savefig('input_output\expt3_dpi_300.jpg',dpi=300)
# plt.show()

# fig3=plt.figure(3,dpi=150)
# plt.axis('off')
# plt.imshow(img1,cmap='gray',interpolation='none')
# fig2.savefig('input_output\expt3_dpi_150.jpg',dpi=150)
# plt.show()

# fig4=plt.figure(4,dpi=72)
# plt.axis('off')
# plt.imshow(img1,cmap='gray',interpolation='none')
# fig2.savefig('input_output\expt3_dpi_72.jpg',dpi=72)
# plt.show()

'''Getting the generated images with reduced spatial resolution '''

img1250=plt.imread('input_output\expt3_dpi_1250.jpg')
img300=plt.imread('input_output\expt3_dpi_300.jpg')
img150=plt.imread('input_output\expt3_dpi_150.jpg')
img72=plt.imread('input_output\expt3_dpi_72.jpg')

''' Displaying the output '''

fig5=plt.figure(5)
gs1=gs.GridSpec(2,2)

ax11=plt.subplot(gs1[0,0])
ax11.set_title("1250 dpi")
ax11.axis("off")
ax11.imshow(img1250,cmap='gray')

ax12=plt.subplot(gs1[0,1])
ax12.set_title("300 dpi")
ax12.axis("off")
ax12.imshow(img300,cmap='gray')

ax13=plt.subplot(gs1[1,0])
ax13.set_title("150 dpi")
ax13.axis("off")
ax13.imshow(img150,cmap='gray')

ax14=plt.subplot(gs1[1,1])
ax14.set_title("72 dpi")
ax14.axis("off")
ax14.imshow(img72,cmap='gray')

plt.suptitle('Typical Effects of Reducing Spatial Resolution',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=0.5)
plt.savefig('input_output/expt3.jpg',dpi=1250)
plt.show()  
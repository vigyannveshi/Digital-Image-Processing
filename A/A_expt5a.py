'''
A_expt No. 5: 

Title: Arithmetic Operations in Digital Image Processing using Python 

Aim: To write a program using Python to perform the following:
a) Addition (Averaging) of noisy images for noise reduction
b) Image Subtraction for Enhancing Differences
c) Image Subtraction for Angiography
d) Image Multiplication for Shading Correction
e) Image Multiplication for 'Region of Interest' (ROI) Operations

'''

'''
Notes:

nil :noise_img_list
v   :variance

'''
# Important imports:
from matplotlib import pyplot as plt, gridspec as gs

### adding path to dip_toolbox
import sys
sys.path.append('./')

from dip_toolbox import NoiseModels

'''a) Addition (Averaging) of noisy images for noise reduction'''

# importing image
img1=plt.imread('CH02\Fig0226(galaxy_pair_original).tif')

### Generating set of noisy images:
''' Added noise: zero mean random gaussian noise'''

def gen_noisy_img(img,n,mean,variance):
    noisy_img_list=[]
    nm=NoiseModels()
    for _ in range(n):
        noisy_img=nm.gaussian_noise(img.shape,mean,variance)
        noisy_img_list.append(nm.add_noise(noisy_img,img))
    return noisy_img_list

def avg_img(img_lst,n):
    for i in range(1,n):
        img_lst[0]+=img_lst[i]
    return img_lst[0]/n

# Main program 
m=0
v=5*1e3
nil=gen_noisy_img(img1,1000,m,v)


# plots
fig1=plt.figure(1)
gs1=gs.GridSpec(2,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title("Original Image")
ax11.axis("off")
ax11.imshow(img1,cmap='gray')

ax12=plt.subplot(gs1[0,1])
ax12.set_title("One Noisy Image")
ax12.axis("off")
ax12.imshow(nil[0],cmap='gray')

ax13=plt.subplot(gs1[0,2])
ax13.set_title("Averages:10")
ax13.axis("off")
ax13.imshow(avg_img(nil,10),cmap='gray')

ax14=plt.subplot(gs1[1,0])
ax14.set_title("Averages:100")
ax14.axis("off")
ax14.imshow(avg_img(nil,100),cmap='gray')

ax15=plt.subplot(gs1[1,1])
ax15.set_title("Averages:500")
ax15.axis("off")
ax15.imshow(avg_img(nil,500),cmap='gray')

ax16=plt.subplot(gs1[1,2])
ax16.set_title("Averages:1000")
ax16.axis("off")
ax16.imshow(avg_img(nil,1000),cmap='gray')

plt.suptitle(f'Addition (Averaging) of noisy images (mean={m},variance={v}, gaussian noise) for noise reduction',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout(pad=1.2)
fig1.set_size_inches(10, 8)
plt.savefig('input_output/A_expt5_a.jpg',dpi=300,)
fig1.set_size_inches(5, 4)
plt.show()


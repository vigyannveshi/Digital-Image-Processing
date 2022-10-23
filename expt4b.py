'''
To resize QR codes using nearest neighbourhood interpolation

While Generating QR codes, we shall create them with least rescalable scale, this will save space needed for storage and transmission 

After transmission and recieving we shall zoom using nearest neighbourhood interpolation technique and then retrieve the information

'''

# important imports:
import pyqrcode
from matplotlib import pyplot as plt,gridspec as gs
from dip_toolbox import DipTools

# String to be converted to QR code:
s='https://vigyannveshi.netlify.app/'

# Generate QR code:
url=pyqrcode.create(s)
url.png('input_output\expt4b_qr_code.png',scale=1)

qrcode=plt.imread('input_output\expt4b_qr_code.png')

r,c=qrcode.shape
sz=4
ss=.98     # Minimum tested size that can help retrival


# Creating DipTools class:
dip=DipTools()

# Saving shrinked QR code:

plt.imsave('input_output\expt4b_qrcode_shrinked.jpg',dip.nearest_neighbourhood(qrcode,(int(ss*r),int(ss*c))),cmap='gray')

sqrcode=plt.imread('input_output\expt4b_qrcode_shrinked.jpg')
rs,cs=sqrcode.shape[0:2]


# plots
fig1=plt.figure(1)
gs1=gs.GridSpec(1,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title(f'Original QR Code ({r},{c})')
ax11.imshow(qrcode,cmap='gray')

ax11=plt.subplot(gs1[0,1])
ax11.set_title(f'Shrinked QR Code ({rs},{cs})')
ax11.imshow(qrcode,cmap='gray')

ax12=plt.subplot(gs1[0,2])
ax12.set_title(f'Zoomed QR Code ({int(sz*rs)},{int(sz*cs)})')
ax12.imshow(dip.nearest_neighbourhood(qrcode,(sz*rs,sz*cs)),cmap='gray')


plt.suptitle('Resizing QR code using Nearest Neighbourhood Interpolation',font='Times New Roman',fontweight="bold",fontsize=16)
plt.tight_layout()
fig1.set_size_inches(10, 8)
plt.savefig('input_output\expt4b_resizing_qrcode.jpg',dpi=300)
fig1.set_size_inches(5, 4)
plt.show()


# Saving zoomed QR code:
plt.imsave('input_output\expt4b_qrcode_zoomed.jpg',dip.nearest_neighbourhood(qrcode,(sz*rs,sz*cs)),cmap='gray')
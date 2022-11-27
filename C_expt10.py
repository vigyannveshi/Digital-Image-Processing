'''
C_expt No. 10: 

Title: Direct Inverse Filtering

Aim: To write a program using Python to perform direct inverse filtering on an image corrupted by Atmospheric Turbulence Degradation with k=0.0025 (severe turbulence), and passing it through butterworth filter of order 10 and radii:
i)   40
ii)  150
iii) 180
to enhance recovery.
'''

# important imports:
import numpy as np
from matplotlib import pyplot as plt,gridspec as gs
from dip_toolbox import FrequencyDomain,DegradationModels,IntensityTransformations,Filters

# creating objects from the classes imported:
fd=FrequencyDomain()
dm=DegradationModels()
it=IntensityTransformations()
flt=Filters()

# importing the original image:
img1=plt.imread('CH05\Fig0525(a)(aerial_view_no_turb).tif')
img1_f=fd.dftshift2(fd.dft2(img1))


# atmospheric turbulence degradation:
H_st=dm.atm_tur(img1.shape,0.0025)    # Severe Turbulence

# degraded images in frequency domain:
img_f_H_st=img1_f*H_st

# degraded images in spatial domain:
img_s_H_st=fd.idft2(fd.dftshift2(img_f_H_st))

# Inverse filtering and bounding the output using butterworth filter of order 10, and different radii in frequency domain: 
img_f_invf=fd.dftshift2(fd.dft2(img_s_H_st))/H_st
ord=10
img_f_invf_b_40=(img_f_invf)*flt.bw_lp_flt(img_f_invf.shape,40,ord)
img_f_invf_b_150=(img_f_invf)*flt.bw_lp_flt(img_f_invf.shape,150,ord)
img_f_invf_b_180=(img_f_invf)*flt.bw_lp_flt(img_f_invf.shape,180,ord)

# Inverse filtering and bounding the output using butterworth filter of order 10, and different radii in spatial domain: 
img_s_invf=fd.idft2(fd.dftshift2(img_f_invf))
img_s_invf_b_40=fd.idft2(fd.dftshift2(img_f_invf_b_40))
img_s_invf_b_150=fd.idft2(fd.dftshift2(img_f_invf_b_150))
img_s_invf_b_180=fd.idft2(fd.dftshift2(img_f_invf_b_180))


# plots
fig1=plt.figure(1)
gs1=gs.GridSpec(2,3)

ax11=plt.subplot(gs1[0,0])
ax11.set_title('Original image')
ax11.axis('off')
ax11.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax12=plt.subplot(gs1[0,1])
ax12.set_title(f'k=0.0025 (Severe Turbulence)')
ax12.axis('off')
ax12.imshow(img_s_H_st,cmap='gray',vmax=255,vmin=0)

ax13=plt.subplot(gs1[0,2])
ax13.set_title(f'Result of Direct Inverse Filtering (full filter)')
ax13.axis('off')
ax13.imshow(flt.isc(img_s_invf,255),cmap='gray',vmax=255,vmin=0)

ax14=plt.subplot(gs1[1,0])
ax14.axis('off')
ax14.imshow(it.gamma(0.1,255)(np.abs(img1_f)),cmap='gray')

ax15=plt.subplot(gs1[1,1])
ax15.axis('off')
ax15.imshow(it.gamma(0.1,255)(np.abs(img_f_H_st)),cmap='gray')

ax16=plt.subplot(gs1[1,2])
ax16.axis('off')
ax16.imshow(it.gamma(0.1,255)(np.abs(img_f_invf)),cmap='gray')

fig1.tight_layout(pad=2.5)
fig1.set_size_inches(13,8)
fig1.suptitle('Direct Inverse Filtering',font='Times New Roman',fontweight="bold",fontsize=16)
fig1.savefig('input_output/C_expt10_1.jpg',dpi=500)

# plots
fig2=plt.figure(2)
gs2=gs.GridSpec(2,3)

ax21=plt.subplot(gs2[0,0])
ax21.set_title('Result cutoff outside radius of 40')
ax21.axis('off')
ax21.imshow(img_s_invf_b_40,cmap='gray',vmax=255,vmin=0)

ax22=plt.subplot(gs2[0,1])
ax22.set_title(f'Result cutoff outside radius of 150')
ax22.axis('off')
ax22.imshow(img_s_invf_b_150,cmap='gray',vmax=255,vmin=0)

ax23=plt.subplot(gs2[0,2])
ax23.set_title(f'Result cutoff outside radius of 180')
ax23.axis('off')
ax23.imshow(flt.isc(img_s_invf_b_180,255),cmap='gray',vmax=255,vmin=0)


ax24=plt.subplot(gs2[1,0])
ax24.axis('off')
ax24.imshow(it.gamma(0.1,255)(np.abs(img_f_invf_b_40)),cmap='gray')

ax25=plt.subplot(gs2[1,1])
ax25.axis('off')
ax25.imshow(it.gamma(0.1,255)(np.abs(img_f_invf_b_150)),cmap='gray')

ax26=plt.subplot(gs2[1,2])
ax26.axis('off')
ax26.imshow(it.gamma(0.1,255)(np.abs(img_f_invf_b_180)),cmap='gray')

fig2.tight_layout(pad=2.5)
fig2.set_size_inches(13,8)
fig2.suptitle('Output of Direct Inverse Filter, filtered with Butterworth low pass filter: ',font='Times New Roman',fontweight="bold",fontsize=16)
fig2.savefig('input_output/C_expt10_2.jpg',dpi=500)

plt.show()

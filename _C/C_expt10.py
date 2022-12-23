'''
C_expt No. 10: 

Title: Direct Inverse and Weiner Filtering   

Aim: To write a program using Python to perform direct inverse filtering on an image corrupted by Atmospheric Turbulence Degradation with k=0.0025 (severe turbulence), and passing it through butterworth filter of order 10 and radii:
i)   40
ii)  150
iii) 180
to enhance recovery. And compare results with Weiner filtering on the same corrupted image.
with different values of K:
{K=Power Spectrum of Noise / Power Spectrum of Undegraded Image}
i)   1
ii)  0.5
iii) 10^-4
iv)  10^-9
'''

# important imports:
import numpy as np
from matplotlib import pyplot as plt,gridspec as gs

### adding path to dip_toolbox
import sys
sys.path.append('./')

from dip_toolbox import FrequencyDomain,DegradationModels,IntensityTransformations,Filters

# creating objects from the classes imported:
fd=FrequencyDomain()
dm=DegradationModels()
it=IntensityTransformations()
flt=Filters()

# importing the original image:
img1=plt.imread('CH05\Fig0525(a)(aerial_view_no_turb).tif')
img1_f=fd.dftshift2(fd.dft2(img1))

# Degrading the original image:
### atmospheric turbulence degradation:
H_st=dm.atm_tur(img1.shape,0.0025)    # Severe Turbulence

### degraded image in frequency domain:
img_f_H_st=img1_f*H_st

### degraded image in spatial domain:
img_s_H_st=np.real(fd.idft2(fd.dftshift2(img_f_H_st)))


# Recovery from degraded image:
### degraded image in frequency domain:
img_f_deg=fd.dftshift2(fd.dft2(img_s_H_st))

### Inverse filtering and bounding the output using butterworth filter of order 10, and different radii in frequency domain: 
img_f_invf=img_f_deg/H_st
ord=10
img_f_invf_b_40=(img_f_invf)*flt.bw_lp_flt((img_f_invf.shape),40,ord)
img_f_invf_b_150=(img_f_invf)*flt.bw_lp_flt((img_f_invf.shape),150,ord)
img_f_invf_b_180=(img_f_invf)*flt.bw_lp_flt((img_f_invf.shape),180,ord)

### Inverse filtering and bounding the output using butterworth filter of order 10, and different radii in spatial domain: 
img_s_invf=np.real(fd.idft2(fd.dftshift2(img_f_invf)))
img_s_invf_b_40=np.real(fd.idft2(fd.dftshift2(img_f_invf_b_40)))
img_s_invf_b_150=np.real(fd.idft2(fd.dftshift2(img_f_invf_b_150)))
img_s_invf_b_180=np.real(fd.idft2(fd.dftshift2(img_f_invf_b_180)))

### Weiner filtering in frequency domain:
K1=1
K2=0.5
K3=1e-4
K4=1e-9
img_f_wf1=img_f_deg*flt.weiner_flt(H_st,K1)
img_f_wf2=img_f_deg*flt.weiner_flt(H_st,K2)
img_f_wf3=img_f_deg*flt.weiner_flt(H_st,K3)
img_f_wf4=img_f_deg*flt.weiner_flt(H_st,K4)

### Weiner filtering in spatial domain:
img_s_wf1=np.real(fd.idft2(fd.dftshift2(img_f_wf1)))
img_s_wf2=np.real(fd.idft2(fd.dftshift2(img_f_wf2)))
img_s_wf3=np.real(fd.idft2(fd.dftshift2(img_f_wf3)))
img_s_wf4=np.real(fd.idft2(fd.dftshift2(img_f_wf4)))


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
ax13.imshow(img_s_invf,cmap='gray',vmax=255,vmin=0)

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

# # # # # #
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
ax23.imshow(img_s_invf_b_180,cmap='gray',vmax=255,vmin=0)


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
fig2.suptitle('Output of Direct Inverse Filter, cutting off outer radius using Butterworth low pass filter: ',font='Times New Roman',fontweight="bold",fontsize=16)
fig2.savefig('input_output/C_expt10_2.jpg',dpi=500)

# # # # # 
fig3=plt.figure(3)
gs3=gs.GridSpec(2,3)

ax31=plt.subplot(gs3[0,0])
ax31.set_title('Original image')
ax31.axis('off')
ax31.imshow(img1,cmap='gray',vmax=255,vmin=0)

ax32=plt.subplot(gs3[0,1])
ax32.set_title(f'k=0.0025 (Severe Turbulence)')
ax32.axis('off')
ax32.imshow(img_s_H_st,cmap='gray',vmax=255,vmin=0)

ax33=plt.subplot(gs3[0,2])
ax33.set_title(f'Result of Weiner Filtering (K={K1})')
ax33.axis('off')
ax33.imshow(img_s_wf1,cmap='gray',vmax=255,vmin=0)

ax34=plt.subplot(gs3[1,0])
ax34.axis('off')
ax34.imshow(it.gamma(0.1,255)(np.abs(img1_f)),cmap='gray')

ax35=plt.subplot(gs3[1,1])
ax35.axis('off')
ax35.imshow(it.gamma(0.1,255)(np.abs(img_f_H_st)),cmap='gray')

ax36=plt.subplot(gs3[1,2])
ax36.axis('off')
ax36.imshow(it.gamma(0.1,255)(np.abs(img_f_wf1)),cmap='gray')

fig3.tight_layout(pad=2.5)
fig3.set_size_inches(13,8)
fig3.suptitle('Weiner Filtering for different values of K',font='Times New Roman',fontweight="bold",fontsize=16)
fig3.savefig('input_output/C_expt10_3.jpg',dpi=500)

# # # # # 
fig4=plt.figure(4)
gs4=gs.GridSpec(2,3)

ax41=plt.subplot(gs4[0,0])
ax41.set_title(f'Result of Weiner Filtering (K={K2})')
ax41.axis('off')
ax41.imshow(img_s_wf2,cmap='gray',vmax=255,vmin=0)

ax42=plt.subplot(gs4[0,1])
ax42.set_title(f'Result of Weiner Filtering (K={K3})')
ax42.axis('off')
ax42.imshow(img_s_wf3,cmap='gray',vmax=255,vmin=0)

ax43=plt.subplot(gs4[0,2])
ax43.set_title(f'Result of Weiner Filtering (K={K4})')
ax43.axis('off')
ax43.imshow(img_s_wf4,cmap='gray',vmax=255,vmin=0)

ax44=plt.subplot(gs4[1,0])
ax44.axis('off')
ax44.imshow(it.gamma(0.1,255)(np.abs(img_f_wf2)),cmap='gray')

ax45=plt.subplot(gs4[1,1])
ax45.axis('off')
ax45.imshow(it.gamma(0.1,255)(np.abs(img_f_wf3)),cmap='gray')

ax46=plt.subplot(gs4[1,2])
ax46.axis('off')
ax46.imshow(it.gamma(0.1,255)(np.abs(img_f_wf4)),cmap='gray')

fig4.tight_layout(pad=2.5)
fig4.set_size_inches(13,8)
fig4.suptitle('Weiner Filtering for different values of K',font='Times New Roman',fontweight="bold",fontsize=16)
fig4.savefig('input_output/C_expt10_4.jpg',dpi=500)

plt.show()

'''

E_expt No. 1: 

Title: Low Rank Approximations of an Image using SVD

Aim: To write a program using Python the visualize the application of Singular Value Decomposition to achieve low rank approximations of an Image

'''

# important imports 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.animation import FFMpegWriter
from matplotlib.gridspec import GridSpec

# importing image
img=plt.imread('CH02\Fig0241(c)(einstein high contrast).tif')

# performing SVD decomposition of image
U,SG,V_t=np.linalg.svd(img)

# function to get the kth rank image
def get_kth_LRA_image(U,SG,V_t,k):
    vect=lambda A: np.reshape(A,(A.shape[0],1))
    lr_img=np.zeros((U.shape[0],V_t.shape[1]))
    for i in range(k+1):
        lr_img+=(SG[i]*((vect(U[:,i])@vect(V_t[i,:]).T)))
    return lr_img

fig, ax = plt.subplots()
plt.title('Low Rank Approximations of an Image using \n Singular Value Decomposition',{'color':'black','fontweight':'bold','fontsize':12})
plt.axis(False)

ims=[]
lr_img=np.zeros((U.shape[0],V_t.shape[1]))
vect=lambda A: np.reshape(A,(A.shape[0],1))

# Getting frames for video, each frame is kth rank LRA Image
for i in range(0,117):
    t=ax.text(625,50,f'Rank:{i+1}',fontdict={'color':'black','fontweight':'bold','fontsize':12},bbox=dict(facecolor='orange', alpha=0.9))

    lr_img+=(SG[i]*((vect(U[:,i])@vect(V_t[i,:]).T)))
    im=ax.imshow(lr_img,cmap='gray',animated=True)
    ims.append([im,t])

for i in range(118,SG.shape[0],20):
    t=ax.text(625,50,f'Rank:{i+1}',fontdict={'color':'black','fontweight':'bold','fontsize':12},bbox=dict(facecolor='orange', alpha=0.9))

    lr_img+=(SG[i]*((vect(U[:,i])@vect(V_t[i,:]).T)))
    im=ax.imshow(lr_img,cmap='gray',animated=True)
    ims.append([im,t])

ani=animation.ArtistAnimation(fig=fig,artists=ims,interval=500,blit=True)

# Saving the video
metadata=dict(title='Low Rank Approximations of an Image using Singular Value Decomposition',artist='VigyannVeshi')
writer=FFMpegWriter(fps=5,metadata=metadata,bitrate=1800)
ani.save("input_output/E_expt1_1.mp4",writer=writer)

# Plotting The LRA images:
def plot_image(gs_, img_, title_):
    ax_ = plt.subplot(gs_)
    ax_.imshow(img_,cmap='gray')
    ax_.set_title(title_)
    ax_.axis(False)

# Saving images have low rank approximated images
fig2=plt.figure(2)
fig2.suptitle('Low Rank Approximations of an Image using \n Singular Value Decomposition')
gs=GridSpec(3,3)
ranks=[1,10,20,30,50,100,200,400,679]
grid_lst=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
for _ in range(9):
    plot_image(gs[grid_lst[_][0],grid_lst[_][1]],get_kth_LRA_image(U,SG,V_t,ranks[_]-1),f'Rank:{ranks[_]}')
plt.tight_layout()
plt.savefig('input_output/E_expt1_2.png',dpi=300)

plt.show()

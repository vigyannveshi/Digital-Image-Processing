'''
The class is created for simplifying the plots
'''

from matplotlib import pyplot as plt, gridspec as gs

class PlottingFunctions:
    def __init__(self):
        self.show=lambda : plt.show()

    def plot(self,img_lst,titles,fig_no,gd,fig_title,save_title,fig_size=(13,8),fig_pad=2,fig_font='Times New Roman',fig_fontweight="bold",fig_fontsize=16,fig_dpi=500,grid=False,axis=False,g_hspace=None,g_wspace=None):
        fig=plt.figure(fig_no)
        i,j=gd
        n=0
        gs_=gs.GridSpec(i,j,hspace=g_hspace,wspace=g_wspace)
        for k in range(i):
            for l in range(j):
                ax=plt.subplot(gs_[k,l])
                ax.set_title(titles[n])
                ax.axis(axis)
                ax.grid(grid)
                ax.imshow(img_lst[n],cmap='gray',vmax=255,vmin=0)
                n+=1
        fig.tight_layout(pad=fig_pad)
        fig.set_size_inches(fig_size)
        fig.suptitle(fig_title,font=fig_font,fontweight=fig_fontweight,fontsize=fig_fontsize)
        fig.savefig('input_output/'+save_title,dpi=fig_dpi)

    
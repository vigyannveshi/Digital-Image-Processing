'''
Intensity Transformations
'''
# Important imports
import numpy as np

class IntensityTransformations:

    def __init__(self):
        pass


    ''' Bit plane Slicing '''
    def bit_plane_slicing(self, img):
        '''
        img_bps[n]--> gives nth bit plane
        '''
        img_bps_lst = []
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                img_bps_lst.append(np.binary_repr(img[i][j], width=8))
        img_bps = []
        for j in range(0,8):
            img_bps.append((np.array([int(i[7-j]) for i in img_bps_lst],dtype=np.uint8)*(2**j)).reshape(img.shape[0], img.shape[1]))
        return img_bps


    ''' Contrast Stretching '''
    def contrast_stretch(self,r1,r2,s1,s2,L=256):
        def cs(r):
            if r>=0 and r<r1:
                return (s1*r)/r1
            elif r>=r1 and r<=r2:
                return (r-r1)*((s2-s1)/(r2-r1))+s1
            elif r>r2 and r<L-1:
                return (r-r2)*((L-1-s2)/(L-1-r2))+s2
        return np.vectorize(cs)


    ''' Thresholding '''
    def threshold(self,m,L=256):
        def thr(r):
            if r<=m:
                return 0
            else: 
                return L-1
        return np.vectorize(thr)


    ''' Image Negative '''
    def negative(self,img,L):
        img=np.uint8(img)
        return self.contrast_stretch(0,L-1,L-1,0)(img)


    ''' Intensity Level Slicing '''
    def intensity_level_slice(self,a,thr,b,s=0):
        def ils(r):
            if r in range(*a):
                return b
            else:
                if thr==0:
                    return s
                else:
                    return r
        
        return np.vectorize(ils)


    ''' Log Transformations (base:n)'''
    def log(self,L,base=10,max_val=None):
        if max_val==None:
            max_val=L
        def lg(r):
            c=(L-1)/(np.log(max_val)/np.log(base))
            return c*(np.log(1+r)/np.log(base))
        
        return np.vectorize(lg)


    ''' Antilog Transformations (base:n)'''
    def antilog(self,L,base=10,e=0,max_val=None):
        if max_val==None:
            max_val=L
        def alg(r):
            c=(np.log(max_val)/np.log(base))/(L-1+e)
            return (base**((r+e)*c))-1
        return np.vectorize(alg)


    ''' Power-Law (Gamma) Transformations'''
    def gamma(self,q,L,max_val=None,e=0):
        if max_val==None:
            max_val=L-1
        def gm(r):
            c=(max_val)/((L-1+e)**q)
            return c*((r+e)**q)
        return np.vectorize(gm)
        
    

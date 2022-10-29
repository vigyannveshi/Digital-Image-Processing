'''
Noise Models includes:
a) Gaussian Noise
b) Uniform Noise
c) Impulse (salt and pepper) noise
f) Erlang Noise
d) Exponential Noise
e) Rayleigh Noise


'''
# important imports:
import numpy as np
from scipy import stats as st
import cv2 as cv

class NoiseModels:

    def __init__(self):
        # Gaussian Noise
        self.gaussian_noise=lambda mean,variance,size: np.random.normal(loc=mean,scale=np.sqrt(variance),size=size)
        
        # Uniform Noise:
        self.uniform_noise=lambda size,a,b:np.random.uniform(low=a,high=b,size=size)

        # Rayleigh Noise:
        self.rayleigh_noise=lambda size,a,b:st.rayleigh(a,b).rvs(size=size)

        # Erlang Noise:
        self.erlang_noise=lambda size, a,beta:st.gamma(a,scale=1/beta).rvs(size=size)
        
        # Exponential Noise:
        self.exponential_noise=lambda size,beta:st.expon(scale=1/beta).rvs(size=size)


    def salt_pepper_noise(self,img,pp,ps):
        sp_img=np.copy(img)
        r,c=sp_img.shape
        pn_pxls=np.uint64(pp*r*c)
        sn_pxls=np.uint64(ps*r*c)
        locs=([(x,y) for x in range(0,r) for y in range(0,c)])
        np.random.shuffle(locs)
        pn_locs=locs[0:pn_pxls]
        locs=locs[::-1]
        sn_locs=locs[0:sn_pxls]
        
        for i in pn_locs:
            sp_img[i]=0
        for j in sn_locs:
            sp_img[j]=255
        
        return sp_img

    def add_noise(self,noise,img):
        return cv.add(noise, img, dtype=cv.CV_64F)

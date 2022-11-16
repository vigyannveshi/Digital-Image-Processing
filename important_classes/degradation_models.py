'''
Degradation Models includes:
a) Atmospheric Turbulence
b) Motion Blur

'''

# important imports:
import numpy as np

class DegradationModels:
    def __init__(self):
        pass

    def atm_tur(self,img_shape,k):
        '''
        Atmospheric Turbulence: 
        Hufnagel and Stanley (1964)
        H(u,v)=e^(-k)(u^2+v^2)--> Rafael C. Gonzalez | Richard E. Woods
        The problem with above filter is that it is not centered at center of image for applying it.
        So we need to shift it at center hence the expression:
        H(u,v)=e^(-k)((u-M/2)^2+(v-N/2)^2)--> Rafael C. Gonzalez | Richard E. Woods, inspired from Gaussian LPF as mentioned in theory
        '''
        H=np.zeros(img_shape,dtype=np.float32)
        M,N=img_shape
        for u in range(M):
            for v in range(N):
                H[u,v]=np.exp(-k*(((u-M/2)**2+(v-N/2)**2)**(5/6)))
        return H
    

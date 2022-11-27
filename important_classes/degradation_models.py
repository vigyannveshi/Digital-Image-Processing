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
        ## Atmospheric Turbulence ##
        Hufnagel and Stanley (1964)
        H(u,v)=e^(-k)((u-M/2)^2+(v-N/2)^2)--> Reference: Rafael C. Gonzalez | Richard E. Woods 
        '''
        H=np.zeros(img_shape,dtype=np.float64)
        M,N=img_shape
        for u in range(M):
            for v in range(N):
                H[u,v]=np.exp(-k*(((u-M/2)**2+(v-N/2)**2)**(5/6)))
        return H
    
    def motion_blur(self, img_shape,a,b,T):
        '''
        ## Motion Blur ##
        Assumptions: 
        1) Image undergoes uniform linear motion in x - direction at rate
        x0(t)=at/T; and uniform linear motion in y - direction at rate 
        y0(t)=bt/T; for duration of T seconds, hence image is displaced by 
        root(a^2+b^2) units.
        H[u,v]=(T/(np.pi*((u-M/2)*a+(v-N/2)*b)))*(np.sin(np.pi*((u-M/2)*a+(v-N/2)*b)))*np.exp(-1j*((u-M/2)*a+(v-N/2)*b))--> Reference: Rafael C. Gonzalez | Richard E. Woods 
        '''
        H=np.zeros(img_shape,dtype=complex)
        M,N=img_shape
        for u in range(M):
            for v in range(N):
                if ((u-M/2)*a+(v-N/2)*b)==0:
                    H[u,v]=1
                else:
                    H[u,v]=(T/(np.pi*((u-M/2)*a+(v-N/2)*b)))*(np.sin(np.pi*((u-M/2)*a+(v-N/2)*b)))*np.exp(-1j*((u-M/2)*a+(v-N/2)*b))
        return H
'''
Frequency Domain:

Methods:
    # getW              : returns Vandermonde matrix for order n
    # dft               : used to calculate 1D Discrete Fourier Transform
    # idft              : used to calculate 1D Inverse Discrete Fourier Transform
    # dftshift          : used to center the 1D DFT
    # dft2              : used to calculate 1D Discrete Fourier Transform
    # idft2             : used to calculate 1D Inverse Discrete Fourier Transform
    # pad_img           : pads the image (Needed to avoid wrap around error)
    # unpad_img         : un-pads the padded image
    # apply_freq_flt    : used to apply frequency domain filter (Takes care of Wrap Around Error)

'''

# Important imports
import numpy as np
from matplotlib import pyplot as plt
    

class FrequencyDomain:

    def __init__(self):
        self.flt_size=lambda img_shape: (2*img_shape[0],2*img_shape[1])


    # Vandermonde matrix

    def getW(self,N):
        W=np.zeros((N,N),dtype=complex)
        for n in range(0,N):
            for k in range(0,N):
                W[n][k]=np.exp((-2j*np.pi*n*k)/N)
        return W

    # 1D - Discrete Fourier Transform

    def dft(self,xn,N=None):
        if N==None:
            N=len(xn)
        else:
            if len(xn)>=N:
                xn=xn[:N]
            else:
                xn=np.append(xn,np.zeros(N-len(xn)))

        return np.dot(xn,self.getW(N))


    def idft(self,Xk,N=None):
        if N==None:
            N=len(Xk)
        Wct=np.conjugate(np.transpose(self.getW(N)))
        return np.dot(Xk,Wct)/N

    def dftshift(self,Xk):
        sXk=np.zeros(Xk.shape,dtype=complex)
        sXk[:np.uint64(len(Xk)/2)] = Xk[:np.uint64(len(Xk)/2)][::-1]
        sXk[np.uint64(len(Xk)/2):] = Xk[np.uint64(len(Xk)/2):][::-1]
        return sXk
    
    # 2D - Discrete Fourier Transform
    def dft2(self,xyn,M=None,N=None):
        if M==None and N==None:
            M,N=np.array(xyn).shape
        if M>N:
            W_M=self.getW(M)
            W_N=W_M[0:N,0:N]
        else:
            W_N=self.getW(N)
            W_M=W_N[0:M,0:M]
        return np.transpose(np.dot(np.transpose(np.dot(xyn,W_N)),W_M))

    def dftshift2(self,xyk):
        return np.transpose(self.dftshift(np.transpose(self.dftshift(xyk))))

    def idft2(self,XYK,M=None,N=None):
        if M==None and N==None:
            M,N=np.array(XYK).shape
        if M>N:
            Wct_M=np.conjugate(np.transpose(self.getW(M)))
            Wct_N=Wct_M[0:N,0:N]
        else:
            Wct_N=np.conjugate(np.transpose(self.getW(N)))
            Wct_M=Wct_N[0:M,0:M]

        return np.transpose(np.dot(np.transpose(np.dot(XYK,Wct_N)),Wct_M))/(M*N)

    # Apply Frequency Domain filter

    def pad_img(self,img):
        r,c=img.shape
        img_pd=np.zeros((2*r,2*c))
        img_pd[:r,:c]=img
        return img_pd
    
    def unpad_img(self,img_pd):
        r,c=img_pd.shape
        img_unpd=img_pd[:int(r/2),:int(c/2)]
        return img_unpd

    def apply_freq_flt(self,img,flt):
        '''
        img: image (could be in spatial or frequency)
        flt: filter
        input: 0 --> image in spatial domain (default)
               1 --> image in frequency domain (already padded in spatial domain and then dft is found, transform translated to center )  
        '''

        # Step 1: Pad the image with zeroes such that it has a size of (2r,2c)
        img=self.pad_img(img)
        r,c=img.shape

        # Step 2: Multiply by (-1)^(x+y) to translate center its transform
        freq_trans=np.array([(-1)**(x+y) for x in range(r) for y in range(c)]).reshape(r,c)
        img=img*freq_trans

        # Step 3: Compute the DFT of image F(u,v)
        F=self.dft2(img)

        # Step 4: Generate a real, symmetric filter function H(u,v) of size (r,c) with center at (r/2,c/2)
        H=flt

        # Step 5: Form the product G(u,v)=H(u,v)*F(u,v)
        G=H*F
        
        # Step 6: Obtain the processed image: gp(x,y)={real(=[IDFT(G(u,v))])}*(-1)^(x+y)
        g=np.real(self.idft2(G))*freq_trans

        # Step 7: Return the frequency domain and unpaded spatial domain filtered image
        return (G,self.unpad_img(g))           
    
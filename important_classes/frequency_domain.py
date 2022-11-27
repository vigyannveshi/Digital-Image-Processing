'''
Frequency Domain:
'''

# Important imports
import numpy as np
    

class FrequencyDomain:

    def __init__(self):
        pass


    # 1D - Discrete Fourier Transform

    def getW(self,N):
        W=np.zeros((N,N),dtype=complex)
        for n in range(0,N):
            for k in range(0,N):
                W[n][k]=np.exp((-2j*np.pi*n*k)/N)
        return W


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
        return np.abs(np.dot(Xk,Wct)/N)

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
        return np.abs(np.transpose(np.dot(np.transpose(np.dot(XYK,Wct_N)),Wct_M))/(M*N))
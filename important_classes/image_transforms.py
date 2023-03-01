import numpy as np

class ImageTransforms:

    def __init__(self):
        pass

    '''Transformation matrices:'''

    # Vandermonde matrix (Used as basis function for Discrete Fourier Transforms)
    def W(self,N):
        W=np.zeros((N,N),dtype=complex)
        for n in range(0,N):
            for k in range(0,N):
                W[n][k]=np.exp((-2j*np.pi*n*k)/N)
        return W


    '''1D Unitary transform'''

    def uni_tf(self,xn,TF,N=None):
        if N==None:
            N=len(xn)
        else:
            if len(xn)>=N:
                xn=xn[:N]
            else:
                xn=np.append(xn,np.zeros(N-len(xn)))

        return np.dot(xn,TF(N))
    
    def inv_uni_tf(self,Xk,TF,N=None):
        if N==None:
            N=len(Xk)
        ITF=np.conjugate(np.transpose(TF(N)))
        return np.dot(Xk,ITF)


    '''2D Unitary Transform'''

    def uni_tf2(self,xyn,TF,M=None,N=None):
        if M==None and N==None:
            M,N=np.array(xyn).shape
        if M>N:
            akm=TF(M)
            anl=akm[0:N,0:N]
        else:
            anl=TF(N)
            akm=anl[0:M,0:M]
        return np.transpose(np.dot(np.transpose(np.dot(xyn,anl)),akm))

    def inv_uni_tf2(self,XYK,TF,M=None,N=None):
        if M==None and N==None:
            M,N=np.array(XYK).shape
        if M>N:
            amk=np.conjugate(np.transpose(TF(M)))
            aln=amk[0:N,0:N]
        else:
            aln=np.conjugate(np.transpose(TF(N)))
            amk=aln[0:M,0:M]

        return np.transpose(np.dot(np.transpose(np.dot(XYK,aln)),amk))
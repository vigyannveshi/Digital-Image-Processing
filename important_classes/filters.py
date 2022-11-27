'''
Filters:

    Notes:
    * The contents are designed for gray scale images

    # height         : no of rows in image
    # width          : no of columns in image    
    # r              : height of original image
    # c              : width of original image
    # d_h            : needed height of padding /selecting neighbourhood
    # d_w            : needed width of padding /selecting neighbourhood
    # m_d_h          : max height of padding /selecting neighbourhood
    # m_d_w          : max width of padding /selecting neighbourhood
    # p_h            : image height after padding 
    # p_w            : image width after padding 
    # size_org       : size of original image
    # imax           : max possible intensity in the image
    # imin           : min possible intensity in the image
    # nh             : neighbourhood


    * Attributes:
        ** Filter Masks:
            *** Smoothening Filter Masks:
                # am_mask           : arithmetic filter mask
                # gaussian_mask     : gaussian filter mask

            *** Smoothening Filters
                # am_flt            : arithmetic mean filter
                # gm_flt            : geometric mean filter
                # hm_flt            : harmonic mean filter
                # chm_flt           : contraharmonic filter

                **** Order Statistic Filters
                    # median_flt    : median filter
                    # max_flt       : max filter
                    # min_flt       : min filter
                    # midpt_flt     : midpoint filter
                    # alptrm_flt    : alpha-trimmed mean filter
                    


    * Methods:
        ** Pre-Post Processing
            # pad_img           : used to pad an image
            # unpad_img         : used to unpad a padded image
            # isc               : intensity scaling correction
        
        ** Applying Filters / Masks
            # flt_apply           : used to apply filters by passing flts / masks and image
        
        ** Adaptive Filters
            # adpt_median_flt           : adaptive median filter
            # adpt_lclnr_flt            : adaptive local noise reduction filter 
        
        ** Frequency Domain Filters
            # glp_flt                   :Gaussian Low pass filter
            # ghp_flt                   :Gaussian High pass filter



'''

# Important imports
import numpy as np

class Filters():

    def __init__(self):
        '''Filter masks: Smoothening'''
        self.am_mask=lambda order:(1/(order**2))*np.ones((order,order))
        self.guassian_mask=lambda order,sigma:np.array([np.exp(-(x**2+y**2)/2*(sigma**2)) for x in range(-int(order/2),int(order/2)+1) for y in range(-int(order/2),int(order/2)+1)]).reshape(order,order)

    # # # # # # # # # # # # # # # # # # # # # # # # #
        '''Filter masks: Sharpening'''

        # Laplacian Filters:
        self.lap_mask90_le=np.array([[0,1,0],[1,-4,1],[0,1,0]])
        self.lap_mask90_de=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
        self.lap_mask45_le=np.array([[1,1,1],[1,-8,1],[1,1,1]])
        self.lap_mask45_de=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

        self.line_mask_x=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
        self.line_mask_y=np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
        self.line_mask_pxy=np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
        self.line_mask_nxy=np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])

        # Prewitt Filters:
        self.prew_mask_x=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
        self.prew_mask_y=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        self.prew_mask_pxy=np.array([[0,1,1],[-1,0,1],[-1,-1,0]])
        self.prew_mask_nxy=np.array([[-1,-1,0],[-1,0,1],[0,1,1]])

        # Sobel Filters:
        self.sobel_mask_x=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
        self.sobel_mask_y=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        self.sobel_mask_pxy=np.array([[0,1,2],[-1,0,1],[-2,-1,0]])
        self.sobel_mask_nxy=np.array([[-2,-1,0],[-1,0,1],[0,1,2]])

    # # # # # # # # # # # # # # # # # # # # # # # # #
        
        '''Filters: Smoothening'''
        self.am_flt=lambda nh: np.average(nh)

        self.gm_flt=lambda nh: np.abs(np.power(np.prod(nh),(1/nh.size),dtype=complex))

        self.hm_flt=lambda nh: 0 if 0 in nh else np.reciprocal(np.average(np.reciprocal(nh)))

        self.chm_flt=lambda q:lambda nh: 0 if(0 in nh and q<0) else 0 if np.abs(np.sum(np.power(nh,q,dtype=complex)))==0 else np.abs(np.sum(np.power(nh,q+1,dtype=complex)))/np.abs(np.sum(np.power(nh,q,dtype=complex)))
        


        ''' **** Order Statistic Filters'''
        self.median_flt=lambda nh: np.median(nh)
        self.max_flt =lambda nh: np.max(nh)
        self.min_flt=lambda nh: np.min(nh)
        self.midpt_flt=lambda nh: 0.5*(np.max(nh)+np.min(nh))
        self.alptrm_flt=lambda d:lambda nh:np.average(np.sort(np.ravel(nh))[int(d/2):(np.sort(np.ravel(nh)).size-int(d/2))])

    # # # # # # # # # # # # # # # # # # # # # # # # #

    ''' ** Preprocessing and Post Processing functions'''
    def pad_img(self, img, layers, pad_with=0):

        r, c = img.shape[0:2]
        d_h = layers
        d_w = layers
        p_h = r+d_h
        p_w = c+d_w

        if pad_with == 0:
            img_pd = np.zeros((p_h+d_h, p_w+d_h))
        else:
            img_pd = np.ones((p_h+d_h, p_w+d_h))*255

        for i in range(d_h, p_h):
            for j in range(d_w, p_w):
                img_pd[i][j] = img[i-d_h][j-d_w]
        return img_pd

    def unpad_img(self, img, size_org, layers):
        d_h = layers
        d_w = layers
        p_h = size_org[0]+d_h
        p_w = size_org[1]+d_w
        img_unpd = np.zeros((size_org[0], size_org[1]))
        for i in range(d_h, p_h):
            for j in range(d_w, p_w):
                img_unpd[i-d_h][j-d_w] = img[i][j]
        return img_unpd

    def isc(self, img,L):
        imax = np.max(img)
        imin = np.min(img)
        if imin<0:
            img=((img-(np.ones(img.shape)*imin))/imax)*(L-1)
        else:
            img=((img-(np.ones(img.shape)))/imax)*(L-1)
        return img


    # # # # # # # # # # # # # # # # # # # # # # # # #
    ''' ** Applying Filters and Filter Masks'''
    def flt_apply(self, img, ord=None, flt=None, mask=np.array([None]),pad_with=0):
        if mask.any()!=None:
            order=mask.shape[0]
        else: 
            order=ord

        r, c = img.shape[0:2]
        d_h = int((order-1)/2)
        d_w = int((order-1)/2)
        p_h = r+d_h
        p_w = c+d_w

        img_pd = self.pad_img(img, d_h,pad_with=pad_with)
        flt_img = np.zeros(img_pd.shape)

        if mask.any()!=None and flt==None:
            for i in range(d_h, p_h):
                for j in range(d_w, p_w):
                    flt_img[i][j] = np.sum(img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1] * mask)

        elif mask.any()==None and flt!=None:
            for i in range(d_h, p_h):
                for j in range(d_w, p_w):
                    flt_img[i][j] = flt(img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1])


        return self.unpad_img(flt_img, img.shape[0:2], d_h)


    # # # # # # # # # # # # # # # # # # # # # # # # #

    '''** Adaptive Filters'''

    # Adaptive Median Filter:
 
    def adpt_median_flt(self,img,smax,pad_with=0):
        r, c = img.shape[0:2]
        # max window size:
        m_d_h = int((smax-1)/2)
        m_d_w = int((smax-1)/2)
        # padding size:
        p_h = r+m_d_h
        p_w = c+m_d_w

        img_pd = self.pad_img(img, m_d_h,pad_with=pad_with)
        flt_img = np.zeros(img_pd.shape)

        ### Algorithm 
        def admf(img_pd,i,j,m_d_h,m_d_w,d_h,d_w):
            # neighbourhood:
            nh=img_pd[i-d_h:i+d_h+1,j-d_w:j+d_w+1]
            # neighbourhood parameters:
            zmin=np.min(nh)
            zmax=np.max(nh)
            zmed=np.median(nh)
            zxy=img_pd[i,j]

            # Stage A:
            A1=zmed-zmin
            A2=zmed-zmax

            if A1>0 and A2<0:
                # Stage B:
                B1=zxy-zmin
                B2=zxy-zmax
                if B1>0 and B2<0:
                    return zxy
                else: 
                    return zmed
            else:
                if d_h<m_d_h and d_w<m_d_w:
                    d_h+=1
                    d_w+=1
                    return admf(img_pd,i,j,m_d_h,m_d_w,d_h,d_w)
                else: 
                    return zmed

        ### Applying the Algorithm
        for i in range(m_d_h, p_h):
            for j in range(m_d_w, p_w):
                # began with 3*3 neighbourhood:
                d_h=1
                d_w=1

                flt_img[i][j]=admf(img_pd,i,j,m_d_h,m_d_w,d_h,d_w)
        
        return self.unpad_img(flt_img, img.shape[0:2], m_d_h)
                

    # Adaptive Local Noise Reduction Filter:

    def adpt_lclnr_flt(self,img,lcl_ord,pad_with=0):
        r, c = img.shape[0:2]
        d_h = int((lcl_ord-1)/2)
        d_w = int((lcl_ord-1)/2)
        p_h = r+d_h
        p_w = c+d_w

        img_pd = self.pad_img(img, d_h, pad_with=pad_with)
        flt_img = np.zeros(img_pd.shape)

        # Algorithm:
        ### 1) Find the mean and variance of the locality with minimum variance
        varl=[]
        meanl=[]
        for i in range(lcl_ord, r-lcl_ord):
            for j in range(lcl_ord,c-lcl_ord):
                nh=img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1]
                varl.append(np.var(nh))
                meanl.append(np.average(nh))

        var_noise=varl[np.array(varl).argmin()]
        mean_noise=meanl[np.array(varl).argmin()]

        # Applying the Algorithm:
        for i in range(d_h, p_h):
            for j in range(d_w, p_w):
                nrf=var_noise/(np.var(img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1]))
                if nrf>1:
                    nrf=1
                flt_img[i][j] = (img_pd[i,j]-nrf*(img_pd[i][j]-mean_noise))
        return self.unpad_img(flt_img, img.shape[0:2], d_h)


    ''' Frequency Domain Filters'''

    # Ideal lowpass filter:
    def idl_lp_flt(self,img_shape,D0):
        M,N=img_shape
        H=np.zeros((M,N),dtype=np.float32)
        for u in range(M):
            for v in range(N):
                D=np.sqrt((u-M/2)**2+(v-N/2)**2)
                if D<=D0:
                    H[u,v]=1
                else:
                    H[u,v]=0
        return H

    # Ideal highpass filter:
    def idl_hp_flt(self,img_shape,D0):
        '''
        idl_hp_flt=1-idl_lp_flt
        '''
        return 1-self.idl_lp_flt(img_shape,D0)


    # Butterworth filter:
    def bw_lp_flt(self,img_shape,D0,n):
        M,N=img_shape
        H=np.zeros((M,N),dtype=np.float32)
        for u in range(M):
            for v in range(N):
                D=np.sqrt((u-M/2)**2+(v-N/2)**2)
                H[u,v]=1/(1+(D/D0)**(2*n))
        return H


    # Gaussian Low Pass Filter:
    def glp_flt(self,img_shape,D0):
        '''
        D: radius or distance from the center,
        D0: cutoff frequency
        H(u,v)=exp((-D^2(u,v))/2*D0^2)
        D(u,v)=[(u-M/2)^2+(v-N/2)^2]^(1/2)
        '''
        M,N=img_shape
        H=np.zeros((M,N),dtype=np.float32)
        for u in range(M):
            for v in range(N):
                D=np.sqrt((u-M/2)**2+(v-N/2)**2)
                H[u,v]=np.exp(-D**2/(2*D0*D0))
        return H

    # Gaussian High Pass Filter:
    def ghp_flt(self,img_shape,D0):
        '''
        ghp_flt=1-ghp_flt
        '''
        return 1-self.glp_flt(img_shape,D0)
    
    
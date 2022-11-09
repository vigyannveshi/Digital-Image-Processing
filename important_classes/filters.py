'''
Filters:

    Notes:
    * The contents are designed for gray scale images

    # height         : no of rows in image
    # width          : no of columns in image    
    # r              : height of original image
    # c              : width of original image
    # d_h            : needed height of padding
    # d_w            : needed width of padding
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
        
        ** Applying Filter Masks
            # apply_mask        : used to apply filter masks by passing masks and image
        
        *** Adaptive Filters
            # adpt_lcl_nr_flt     : adaptive local noise reduction filter
            # adpt_median_flt     : adaptive median filter



'''

# Important imports
import numpy as np

class Filters():

    def __init__(self):
        '''Filter masks: Smoothening'''
        self.am_mask=lambda order:(1/(order**2))*np.ones((order,order))

        '''Filter masks: Sharpening'''

        # Laplacian Filters:
        self.lap_mask90_le=np.array([[0,1,0],[1,-4,1],[0,1,0]])
        self.lap_mask90_de=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
        self.lap_mask45_le=np.array([[1,1,1],[1,-8,1],[1,1,1]])
        self.lap_mask45_de=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

        self.lap_mask_hori=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
        self.lap_mask_vert=np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
        self.lap_mask_45_diag_45=np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
        self.lap_mask_45_diag_m45=np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])

        # Prewitt Filters:
        self.prew_mask_hori=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
        self.prew_mask_vert=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        self.prew_mask_diag_45=np.array([[0,1,1],[-1,0,1],[-1,-1,0]])
        self.prew_mask_diag_m45=np.array([[-1,-1,0],[-1,0,1],[0,1,1]])

        # Sobel Filters:
        self.sobel_mask_hori=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
        self.sobel_mask_vert=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        self.sobel_mask_diag_45=np.array([[0,1,2],[-1,0,1],[-2,-1,0]])
        self.sobel_mask_diag_m45=np.array([[-2,-1,0],[-1,0,1],[0,1,2]])
        

        
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
        masked_img = np.zeros(img_pd.shape)

        if mask.any()!=None and flt==None:
            for i in range(d_h, p_h):
                for j in range(d_w, p_w):
                    masked_img[i][j] = np.sum(img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1] * mask)
        elif mask.any()==None and flt!=None:
            for i in range(d_h, p_h):
                for j in range(d_w, p_w):
                    masked_img[i][j] = flt(img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1])


        return self.unpad_img(masked_img, img.shape[0:2], d_h)


    # # # # # # # # # # # # # # # # # # # # # # # # #

        
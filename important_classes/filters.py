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
    # isc            : intensity scaling correction


'''

# Important imports
import numpy as np

class Filters():

    def __init__(self):
        '''Filter masks: Smoothening'''
        self.avg_mask=lambda order:(1/(order**2))*np.ones((order,order))


    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''Preprocessing and Post Processing functions'''
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

    def isc(self, img):
        imax = np.max(img)
        imin = np.min(img)
        img = np.uint8(img-(np.ones(img.shape)*(imin/imax)))
        return img


    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''Applying filter masks'''
    def apply_mask(self, img, mask):
        r, c = img.shape[0:2]
        order=mask.shape[0]
        d_h = int((order-1)/2)
        d_w = int((order-1)/2)
        p_h = r+d_h
        p_w = c+d_w

        img_pd = self.pad_img(img, d_h)
        masked_img = np.zeros(img_pd.shape)

        for i in range(d_h, p_h):
            for j in range(d_w, p_w):
                masked_img[i][j] = np.sum(img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1] * mask)

        return self.unpad_img(masked_img, img.shape[0:2], d_h)



    # # # # # # # # # # # # # # # # # # # # # # # # #
    ''' Smoothening Filters: '''

    def avg_flt(self, img, order):
        r, c = img.shape[0:2]
        d_h = int((order-1)/2)
        d_w = int((order-1)/2)
        p_h = r+d_h
        p_w = c+d_w

        img_pd = self.pad_img(img, d_h)
        avg_img = np.zeros(img_pd.shape)

        for i in range(d_h, p_h):
            for j in range(d_w, p_w):
                avg_img[i][j] = np.average(
                    img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1])

        return self.unpad_img(avg_img, img.shape[0:2], d_h)

    def median_flt(self, img, order):
        r, c = img.shape[0:2]
        d_h = int((order-1)/2)
        d_w = int((order-1)/2)
        p_h = r+d_h
        p_w = c+d_w

        img_pd = self.pad_img(img, d_h)
        median_img = np.zeros(img_pd.shape)

        for i in range(d_h, p_h):
            for j in range(d_w, p_w):
                median_img[i][j] = np.median(
                    img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1])

        return self.unpad_img(median_img, img.shape[0:2], d_h)

    def max_flt(self, img, order):
        r, c = img.shape[0:2]
        d_h = int((order-1)/2)
        d_w = int((order-1)/2)
        p_h = r+d_h
        p_w = c+d_w

        img_pd = self.pad_img(img, d_h)
        max_img = np.zeros(img_pd.shape)

        for i in range(d_h, p_h):
            for j in range(d_w, p_w):
                max_img[i][j] = np.max(img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1])

        return self.unpad_img(max_img, img.shape[0:2], d_h)

    def min_flt(self, img, order):
        r, c = img.shape[0:2]
        d_h = int((order-1)/2)
        d_w = int((order-1)/2)
        p_h = r+d_h
        p_w = c+d_w

        img_pd = self.pad_img(img, d_h)
        min_img = np.zeros(img_pd.shape)

        for i in range(d_h, p_h):
            for j in range(d_w, p_w):
                min_img[i][j] = np.min(img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1])

        return self.unpad_img(min_img, img.shape[0:2], d_h)


    # # # # # # # # # # # # # # # # # # # # # # # # #
    

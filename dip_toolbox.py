'''
    Notes:
    * The contents are designed for gray scale images
    * Nearest Neighbourhood interpolation works for both gray scale as well as colored images

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
    # csi            : create scaled image

'''

# Important imports
import numpy as np


class DipTools:

    def __init__(self):
        pass


    ''' Needed Preprocessing and Postprocessing functions '''

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

    ''' Interpolation techniques '''

    def csi(self, img_size):
        if len(img_size)==3:
            rs_img = np.array([[(0, 0, 0)]*img_size[1]]*img_size[0], dtype='uint8')
        else:
            rs_img = np.array([[0]*img_size[1]]*img_size[0], dtype='uint8')
        return rs_img

    def nearest_neighbourhood(self, img, img_size):
        rs_img = self.csi(img_size)
        # Algorithm for nearest neighbourhood interpolation:
        scale_r, scale_c = (
            rs_img.shape[0]/img.shape[0]), (rs_img.shape[1]/img.shape[1])
        for r in range(rs_img.shape[0]):
            for c in range(rs_img.shape[1]):
                rs_img[r, c] = img[int(r/scale_r), int(c/scale_c)]

        return rs_img

    
# # # # # # # # # # # # # # # # # # # # # # # # #

    
    ''' Special functionalities: '''

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
            img_bps.append((np.array([int(i[7-j]) for i in img_bps_lst],
                           dtype=np.uint8)*(2**j)).reshape(img.shape[0], img.shape[1]))
        return img_bps


# # # # # # # # # # # # # # # # # # # # # # # # #


    ''' Filters: '''

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
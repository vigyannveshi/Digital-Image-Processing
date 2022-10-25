'''
# Interpolation Techniques:
    
    Notes:

    * Only the algorithm for Nearest Neighbourhood interpolation is programmed, rest interpolation techniques have been used from predefined functions in Open CV

    * Nearest Neighbourhood interpolation works for both gray scale as well as colored images

    # csi            : create scaled image

'''

# Important imports
import numpy as np

class Interpolation:

    def __init__(self):
        pass


    '''Creating scaled image for interpolation'''
    def csi(self, img_size):
        if len(img_size)==3:
            rs_img = np.array([[(0, 0, 0)]*img_size[1]]*img_size[0], dtype='uint8')
        else:
            rs_img = np.array([[0]*img_size[1]]*img_size[0], dtype='uint8')
        return rs_img


    ''' Nearest Neighbourhood Interpolation'''
    def nearest_neighbourhood(self, img, img_size):
        rs_img = self.csi(img_size)
        # Algorithm for nearest neighbourhood interpolation:
        scale_r, scale_c = (
            rs_img.shape[0]/img.shape[0]), (rs_img.shape[1]/img.shape[1])
        for r in range(rs_img.shape[0]):
            for c in range(rs_img.shape[1]):
                rs_img[r, c] = img[int(r/scale_r), int(c/scale_c)]

        return rs_img

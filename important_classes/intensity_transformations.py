'''
Intensity Transformations
'''
# Important imports
import numpy as np

class IntensityTransformations:

    def __init__(self):
        pass


    '''Bit plane Slicing'''
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
            img_bps.append((np.array([int(i[7-j]) for i in img_bps_lst],dtype=np.uint8)*(2**j)).reshape(img.shape[0], img.shape[1]))
        return img_bps


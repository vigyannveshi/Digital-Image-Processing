'''
MorphologicalTransformations:

'''

# Important imports
import numpy as np

class MorphologicalTransformations():

    def __init__(self):
        pass

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

    ''' ** Applying Kernel'''
    def apply_morp(self,img,kernel_size,opr,pad_with=0):
        order=kernel_size
        r, c = img.shape[0:2]
        d_h = int((order-1)/2)
        d_w = int((order-1)/2)
        p_h = r+d_h
        p_w = c+d_w

        img_pd = self.pad_img(img, d_h,pad_with=pad_with)
        opr_img = np.zeros(img_pd.shape)


        for i in range(d_h, p_h):
            for j in range(d_w, p_w):
                opr_img[i][j] = opr(img_pd[i-d_h:i+d_h+1, j-d_w:j+d_w+1])


        return self.unpad_img(opr_img, img.shape[0:2], d_h)

    '''Morpohological operations'''

    def erode(self,kernel):
        thr=np.sum(kernel)
        def erosion(mask):
            if int(np.sum(mask*kernel)/255)==thr:
                return 255
            else:
                return 0
        return erosion
    
    def dilate(self,kernel):
        thr=1
        def dilation(mask):
            if int(np.sum(mask*kernel)/255)>=thr:
                return 255
            else:
                return 0
        return dilation
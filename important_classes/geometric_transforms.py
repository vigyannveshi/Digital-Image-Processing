'''
Geometric Transformations:

Attributes:
    cen: center           (img: image, cen: (cols/2,rows/2))
    id:  identity 
    sc:  scale            (cx: scale in x, cy: scale in y)
    rt:  rotate           (cen: needs to be calculated, ang: angle in degrees, scale: default scale is 1)
    tr:  translate        (tx: translate in x, ty: translate in y)
    shr: shear            (sv: vertical shear, sh: horizontal shear)

Methods:
    tf: transform         (img:image, mat: tranformation matrix)

Notes:
    -> To get the actual translate transform matrix (theoretical) you will have to take transpose of tr, the matrix is adjusted in order to fit the needs of the openCV library
    -> Same is the case with shr, to get the actual translate transform matrix (theoretical) you will have to take transpose of tr

'''

# Important imports:
import numpy as np
import cv2 as cv

class GeometricTransforms():

    def __init__(self):
        self.cen=lambda img:(img.shape[1]/2,img.shape[0]/2)
        self.id=np.float32([[1,0,0],[0,1,0],[0,0,1]])
        self.sc=lambda cx,cy:np.float32([[cx,0,0],[0,cy,0],[0,0,1]])
        self.rt=lambda cen,ang,scale=1:np.append(cv.getRotationMatrix2D(cen,ang,scale),[0,0,1]).reshape((3,3))
        self.tr=lambda tx,ty:np.float32([[1,0,tx],[0,1,ty],[0,0,1]])
        self.shr=lambda sh,sv:np.float32([[1,sh,0],[sv,1,0],[0,0,1]])

    def tf(self,img,mat):
        '''Apply Transformation'''
        r,c=img.shape
        img=np.float32(img)
        return cv.warpAffine(img,mat[0:2,:],(c,r))

    
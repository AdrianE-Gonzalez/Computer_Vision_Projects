# To implement Median filtering 3x3 and 5x5) on a noisy image. 
# This can be done by finding the window of pixels around the pixel to be changed, sort them, and select the median value as the replacement of that pixel. 
# Apply the algorithm on an impulsive noise of 10% p probability of noise equally divided among salt and pepper.

import mask
import math
import cv2
import numpy as np

# Returns median filtering Image
def apply_median_filter(mask_size,img):
    
    M,N= img.shape
    g=img.copy()
    mask_,sum,m2,n2=mask.create_mask(mask_size)
    mean=[]

    # Loops Through Each Pixel In The Image Being Changed
    for i in range(m2,M-m2):
        for j in range(n2,N-n2):
            sum=0.0
            #Loops Through Mask And Checks For The Median Value
            for x in range(-m2,m2+1):
                for y in range(-n2,n2+1):
                    #Sets Each Value Of Image To The mask_
                    mask_[x+m2][y+n2]=img[i+x][j+y]
                sum=get_mean(mask_)
            # Turns The Mean Value Into A np.uint8
            g[i][j]=np.uint8(sum)

    return g

# Return The Mean Value Of The Mask    
def get_mean(mask_):
    # Converts mask_ From 2d Array To A 1d Array
    mask_=[val for sublist in mask_ for val in sublist]
    # Sorts The List Of Values In The Mask
    mask_.sort()

    # Checks And Returns The Center Index Of The List In mask_ Using Formula: math.ceil(len(mask_)/2)
    return mask_[math.ceil(len(mask_)/2)]

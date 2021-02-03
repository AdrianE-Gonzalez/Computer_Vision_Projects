# To implement the above convolution algorithm (adjusted to Python strengths such as arrays, slicing, etc.). 
# Once implemented, you will apply it on a noisy image (Gaussian noise of your choice of mean and variance) with the following masks:
    
# • Unweighted average of 5x5
# • Weighted average of 5x5
# • Gaussian mask of 5x5

import math
import cv2
import numpy as np
from mask import create_mask

def create_unweighted():

    mask,sum,m2,n2= create_mask(3)
    d=len(mask)

    for x in range(-m2,m2+1):
        for y in range(x,n2+1):
            mask[x + m2][y + n2] =  round(1/((d*d)),3)

            if(x != y):
                mask[y + n2][x + m2] = mask[x + m2][y + n2]
                sum += 2 * mask[x + m2][y + n2]
            else:
                sum += mask[x + m2][y + n2]
    return mask,sum,m2,n2

def create_weighted():
    mask,sum,m2,n2= create_mask(3)
    d=len(mask)

    for x in range(-m2,m2+1):
        for y in range(x,n2+1):
            if (x==math.floor((-m2+(m2+1))/2)) and (y==math.floor((-m2+(m2+1))/2)):
                mask[x + m2][y + n2] =  round(2/((d*d)+1),3)
            else:
                mask[x + m2][y + n2] =  round(1/((d*d)+1),3)
            
            if(x != y):
                mask[y + n2][x + m2] = mask[x + m2][y + n2]
                sum += 2 * mask[x + m2][y + n2]
            else:
                sum += mask[x + m2][y + n2]    
    return mask,sum,m2,n2

def create_gaussian(sigma):
    mask,sum,m2,n2= create_mask(5)

    for x in range(-m2,m2+1):
        for y in range(x,n2+1):
            mask[x + m2][y + n2] =  round(float(float(1) / (2 * math.pi * sigma * sigma)) * float(math.exp(-((x * x) + (y * y)) / (2.0 * sigma * sigma))), 3)
            
            if(x != y):
                mask[y + n2][x + m2] = mask[x + m2][y + n2]
                sum += 2 * mask[x + m2][y + n2]
            else:
                sum += mask[x + m2][y + n2]
    return mask,sum,m2,n2



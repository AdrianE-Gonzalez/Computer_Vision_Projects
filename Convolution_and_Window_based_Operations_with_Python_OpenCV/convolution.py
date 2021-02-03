# To implement the above convolution algorithm (adjusted to Python strengths such as arrays, slicing, etc.). 
# Once implemented, you will apply it on a noisy image (Gaussian noise of your choice of mean and variance) with the following masks:
    
# • Unweighted average of 5x5
# • Weighted average of 5x5
# • Gaussian mask of 5x5

import math
import cv2
import numpy as np
from mask import create_mask

# Returns mask, sum, m2 And n2
# mask Is The Mask Value At Each Coordinate
#   For Unweighted All Values In Mask Equals: 1/mask_size^2, rounded upto 3 decimal places
# sum Is The Variable At Which The Summation Of The Total Mask Sum Is Stored
# m2 And n2 Is The mask_size/2, Set By math.floor
def create_unweighted(mask_size):

    mask,sum,m2,n2= create_mask(mask_size)
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

# Returns mask, sum, m2 And n2
# mask Is The Mask Value At Each Coordinate
#   For Weighted All Values Except The Center Index Of The Mask Equals: 1/(mask_size^2+1), rounded upto 3 decimal places, 
#   The Center Index Is Set To 2/(mask_size^2+1)
# sum Is The Variable At Which The Summation Of The Total Mask Sum Is Stored
# m2 And n2 Is The mask_size/2, Set By math.floor
def create_weighted(mask_size):
    mask,sum,m2,n2= create_mask(mask_size)
    d=len(mask)

    # Loops Through Mask To Set Each Value Of The Mask
    for x in range(-m2,m2+1):
        for y in range(x,n2+1):
            # Checks If Its The Center Index Of The Mask
            # Else It Sets It To Default Formula
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

# Returns mask, sum, m2 And n2
# mask Is The Mask Value At Each Coordinate
#   For Gaussian All Values In Mask Equals To The Formula Provided: (1/pi*sigma^2)*exponent((x^2+y^2)/2*sigma^2), rounded upto 3 decimal places
# sum Is The Variable At Which The Summation Of The Total Mask Sum Is Stored
# m2 And n2 Is The mask_size/2, Set By math.floor
def create_gaussian(mask_size,sigma):
    mask,sum,m2,n2= create_mask(mask_size)

    # Loops Through Mask To Set Each Value Of The Mask
    for x in range(-m2,m2+1):
        for y in range(x,n2+1):
            # Formula Provided From Slides
            mask[x + m2][y + n2] =  round(float(float(1) / (2 * math.pi * sigma * sigma)) * float(math.exp(-((x * x) + (y * y)) / (2.0 * sigma * sigma))), 3)
            
            if(x != y):
                mask[y + n2][x + m2] = mask[x + m2][y + n2]
                sum += 2 * mask[x + m2][y + n2]
            else:
                sum += mask[x + m2][y + n2]
    return mask,sum,m2,n2



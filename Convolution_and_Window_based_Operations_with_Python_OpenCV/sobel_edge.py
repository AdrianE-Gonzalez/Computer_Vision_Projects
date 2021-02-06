# |g(x,y)|=
# |-f(x-1,y-1)-2f(x-1,y)-f(x-1,y+1)+f(x+1,y-1)+2f(x+1,y)+f(x+1,y+1)|+
# |-f(x-1,y-1)-2f(x,y-1)-f(x+1,y-1)+f(x-1,y+1)+2f(x,y+1)+f(x+1,y+1)|

import cv2
import math
import numpy as np
from mask import create_mask
from mask import apply_mask

# Returns Image Filtered To Sobel Edge Based On Formula Provided Above
def apply_sobel_edge(image):

    g=image.copy()
    M,N=image.shape
    sobelx=0
    sobely=0

    # Loops Through Each Image Pixel And Applies Formula To Image
    for x in range(0,M-1):
        for y in range(0,N-1):
            sobelx= abs((-image[x-1][y-1])-(2*image[x-1][y])-(image[x-1][y+1])+(image[x+1][y-1])+(2*image[x+1][y])+(image[x+1][y+1]))
            sobely= abs((-image[x-1][y-1])-(2*image[x][y-1])-(image[x+1][y-1])+(image[x-1][y+1])+(2*image[x][y+1])+(image[x+1][y+1]))
            g[x][y]=np.uint8(abs(sobelx+sobely))
    return g

# Gets sobel_edge Mask Based On x    
def apply_sobel_edge_x(mask_size):

    mask,sum,m2,n2= create_mask(mask_size)
    d=len(mask)

    for x in range(-m2,m2+1):
        for y in range(-n2,n2+1):
            if not((x*x + y*y)==0):
                mask[x + m2][y + n2] =  round(x / (x*x + y*y),3)
            
    return mask,sum,m2,n2

# Gets sobel_edge Mask Based On y    
def apply_sobel_edge_y(mask_size):

    mask,sum,m2,n2= create_mask(mask_size)
    d=len(mask)

    for x in range(-m2,m2+1):
        for y in range(-n2,n2+1):
            if not((x*x + y*y)==0):
                mask[x + m2][y + n2] =  round(y / (x*x + y*y),3)
            
    return mask,sum,m2,n2

# Applies sobel_mask For x And y Combined
# Returns Image Filtered By Sobel Edge
def get_sobel_mask(img,mask_size):
    mask_1,sum_1,m2_1,n2_1= apply_sobel_edge_x(mask_size=mask_size)
    mask_2,sum_2,m2_2,n2_2= apply_sobel_edge_y(mask_size=mask_size)
    
    mask_=mask_1+mask_2
    sobel= apply_mask(img, mask_,sum_1,m2_1,n2_1)

    return sobel
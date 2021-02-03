# |g(x,y)|=
# |-f(x-1,y-1)-2f(x-1,y)-f(x-1,y+1)+f(x+1,y-1)+2f(x+1,y)+f(x+1,y+1)|+
# |-f(x-1,y-1)-2f(x,y-1)-f(x+1,y-1)+f(x-1,y+1)+2f(x,y+1)+f(x+1,y+1)|

import cv2
import math
import numpy as np

# Returns Image Filtered To Sobel Edge Based On Formula Provided Above
def apply_sobel_edge(image):

    g=image.copy()
    M,N=image.shape
    abs_form=0

    # Loops Through Each Image Pixel And Applies Formula To Image
    for x in range(0,M-1):
        for y in range(0,N-1):
            abs_form= abs(abs((-image[x-1][y-1])-(2*image[x-1][y])-(image[x-1][y+1])+(image[x+1][y-1])+(2*image[x+1][y])+(image[x+1][y+1]))+abs((-image[x-1][y-1])-(2*image[x][y-1])-(image[x+1][y-1])+(image[x-1][y+1])+(2*image[x][y+1])+(image[x+1][y+1])))
            g[x][y]=np.uint8(abs(abs_form))
    return g
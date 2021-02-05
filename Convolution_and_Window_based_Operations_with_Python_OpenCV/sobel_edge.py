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
    sobelx=0
    sobely=0

    # Loops Through Each Image Pixel And Applies Formula To Image
    for x in range(0,M-1):
        for y in range(0,N-1):
            sobelx= abs((-image[x-1][y-1])-(2*image[x-1][y])-(image[x-1][y+1])+(image[x+1][y-1])+(2*image[x+1][y])+(image[x+1][y+1]))
            sobely= abs((-image[x-1][y-1])-(2*image[x][y-1])-(image[x+1][y-1])+(image[x-1][y+1])+(2*image[x][y+1])+(image[x+1][y+1]))
            g[x][y]=np.uint8(abs(sobelx+sobely))
    return g
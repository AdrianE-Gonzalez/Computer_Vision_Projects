import cv2
import numpy as np
import math

# Returns A Empty Mask Based On Size Give, Sum, m2, And n2
# m2 And n2 Are Variables Set Half The Size Given
# Size is set to either 5 for a 5x5 mask
# or 3 for a 3x3 mask
def create_mask(size):
    
    # mask = [[]]
    mask = [[0 for i in range(size)] for i in range(size)]
    sum=0.0
    
    m2= int(math.floor(size/2))
    n2= int(math.floor(size/2))

    return mask,sum,m2,n2

# Returns A New Image Given The Masked Applied
def apply_mask(img,mask,sum,m2,n2):

    M,N=img.shape
    g=img.copy()

   # Loops Through Each Pixel In The Image Being Changed
    for i in range(m2,M-m2):
        for j in range(n2,N-n2):
            sum=0.0
            #Loops Through Mask Being Applied To The Image
            for x in range(-m2,m2+1):
                for y in range(-n2,n2+1):
                    sum+=mask[x+m2][y+n2]*img[i+x][j+y]
                    
            g[i][j]=(sum).clip(0,255).astype(np.uint8)

    # Loops Through The Outer Edge Of Image That Did Not Changed From The Mask,
    # Change It To The Specified Color: 255
    for i in range(0,M):
        for j in range(0,N):
            if i<m2 or i>=(M-m2):
                g[i][j]=np.uint8(255)
            elif j<n2 or  j>=(N-n2):
                g[i][j]=np.uint8(255)

    return g
# Thresholding:
#               g(x,y)={255 if f(x,y)>128 }
#                      {0   otherwise     }

import cv2
import numpy as np

# Converts To A Threshhold Image Using Formula
def threshhold_image(image,looping):
    # Converts Full IMage Using Formula
    def formula():
        threshhold = np.where(image > 128,255,0)
        threshhold = threshhold.clip(0,255).astype(np.uint8)

        return threshhold
    
    # Loops Through Each Pixel And Converts Based On Formula
    def looping_formula():
        rows, cols = image.shape
        threshhold = image.copy()
        
        for r in range(rows):
            for c in range(cols):
                threshhold[r][c]= 255 if image[r][c] > 128 else 0

        return threshhold

    threshhold = looping_formula() if looping else formula()

    return threshhold

# Threshhold LUT Table
def create_lut_threshhold():
    lut=[]
    for i in range(256):
        lut.append(255 if (i>128) else 0)
    return lut

# Converts Image To Threshhold Using LUT(look up table)
def threshhold_image_LUT(image):
    lut_threshhold  = create_lut_threshhold()
    rows, cols = image.shape
    threshhold_LUT = image.copy()
    
    # Iterates Through Image Pixels And Converts Image Based On LUT
    for r in range(rows):
        for c in range(cols):
            threshhold_LUT[r][c]=lut_threshhold[image[r][c]]

    return threshhold_LUT
# Thresholding:
#               g(x,y)={255 if f(x,y)>128 }
#                      {0   otherwise     }

import cv2
import numpy as np

# Converts To A Threshhold Image Using Formula
def threshhold_image(image):
    threshhold = np.where(image > 128,255,0)
    threshhold = threshhold.clip(0,255).astype(np.uint8)
    
    return threshhold

# Converts To A Threshhold Image Using LUT(look up table)
def threshhold_image_LUT(img):
    print()
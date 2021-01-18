# Log transform:
#               g(x,y)={c log10 (1+x)}

import cv2
import numpy as np

# Log Transform Image Using Formula
def log_transform_image(image, looping):
    # Converts Full IMage Using Formula
    def formula():
        log_transform = 1*np.log10(1+image)
        log_transform = log_transform.clip(0,255).astype(np.uint8)

        return log_transform
    # Loops Through Each Pixel And Converts Based On Formula
    def looping_formula():
        rows, cols = image.shape
        log_transform = image.copy()
        
        for r in range(rows):
            for c in range(cols):
                log_transform[r][c]= 1*np.log10(1+image[r][c]) 
        
        return log_transform

    log_transform = looping_formula() if looping else formula()
    
    return log_transform


# Log Transform LUT Table
def create_lut_log_transform():
    lut=[]
    for i in range(256):
        lut.append(1*np.log10(1+i))
    return lut

# Converts Image To Log Transform Using LUT(look up table)
def log_transform_image_LUT(image):
    lut_log_transform  = create_lut_log_transform()
    rows, cols = image.shape
    log_transform_LUT = image.copy()

    # Iterates Through Image Pixels And Converts Image Based On LUT
    for r in range(rows):
        for c in range(cols):
            log_transform_LUT[r][c]=lut_log_transform[image[r][c]]

    return log_transform_LUT
# Negative image:
#               g(x,y)={255-f(x,y)}
import cv2
import numpy as np

# Converts To A Negative Image Using Formula
def negative_image(image,looping):
    # Converts Full IMage Using Formula
    def formula():
        negative = 255-image
        negative = negative.clip(0,255).astype(np.uint8)

        return negative
    # Loops Through Each Pixel And Converts Based On Formula
    def looping_formula():
        rows, cols = image.shape
        negative = image.copy()
        
        for r in range(rows):
            for c in range(cols):
                negative[r][c]= 255 - image[r][c]  

        return negative

    negative = looping_formula() if looping else formula()

    return negative



# Negative LUT Table
def create_lut_negative():
    lut=[]
    for i in range(256):
        lut.append(255-i)
    return lut

# Converts Image To Negative Using LUT(look up table)
def negative_image_LUT(image):
    lut_negative  = create_lut_negative()
    rows, cols = image.shape
    negative_LUT = image.copy()
    
    # Iterates Through Image Pixels And Converts Image Based On LUT
    for r in range(rows):
        for c in range(cols):
            negative_LUT[r][c]=lut_negative[image[r][c]]

    return negative_LUT

# Negative image:
#               g(x,y)={255-f(x,y)}
import cv2
import numpy as np

# Converts To A Negative Image Using Formula
def negative_image(image):
    negative = 255-image
    negative = negative.clip(0,255).astype(np.uint8)

    return negative

# Converts To A Negative Image Using LUT(look up table)
def negative_image_LUT(image):
    print()
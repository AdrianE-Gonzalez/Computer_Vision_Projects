# Log transform:
#               g(x,y)={c log10 (1+x)}

import cv2
import numpy as np

# Log Transform Image Using Formula
def log_transform_image(image):
    
    log_transform = 1*np.log10(1+image)
    log_transform = log_transform.clip(0,255).astype(np.uint8)

    return log_transform

# Log Transform Image sing LUT(look up table)
def log_transform_image_LUT(image):
    print()
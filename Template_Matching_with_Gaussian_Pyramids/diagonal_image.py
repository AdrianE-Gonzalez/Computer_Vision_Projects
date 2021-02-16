from PIL import Image
import numpy as np
import cv2

def get_diagonal(image_list):
    M,N= image_list[0].shape
    if M<=32:
        M,N= M*12,N*12
    background_image= image = np.zeros((M*2,N*2,3), dtype="uint8")
    background_image = Image.fromarray(background_image)

    x_offset = 0

    for im in image_list:
        M,N= im.shape
        
        if M<=32:
            im= cv2.resize(im,(M*12,N*12))

        M,N= im.shape

        im= Image.fromarray(im)
        background_image.paste(im, (x_offset,x_offset))
        x_offset += M

    background_image= np.asarray(background_image)
    return background_image
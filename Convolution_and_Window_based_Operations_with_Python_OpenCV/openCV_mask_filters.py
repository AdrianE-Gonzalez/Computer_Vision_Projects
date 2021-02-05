import cv2


def get_unweighted(img,mask_size):
    unweighted= cv2.blur(img,ksize=(mask_size,mask_size))
    
    return unweighted

def get_weighted(img,mask_size):
    print()

def get_gauss(img,mask_size,sigma):
    #
    gauss= cv2.GaussianBlur(img,(mask_size,mask_size),sigma)
    
    return gauss

def get_median(img,mask_size):
    # 
    median= cv2.medianBlur(img,mask_size)

    return median

def get_sobel(img, mask_size):
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=mask_size)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=mask_size)
    
    return sobelx+sobely

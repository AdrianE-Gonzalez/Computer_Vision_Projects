import cv2
import math 
import load_image

import convolution
import sobel_edge
import noise
import mask

for x in [1]:
    images=load_image.open_multiple_images(x)

    for img in images.values():
        
        img_noise=noise.add_gaussian_noise(50,100,img)
        img_s_p=noise.add_saltpepper_noise(img)

        mask_used,sum,m2,n2= convolution.create_gaussian(sigma=1)
        mask_used2,sum2,m22,n22= convolution.create_unweighted()
        print(mask_used2)
        print("EMPTY SPACE")

        img2= mask.apply_mask(img_s_p, mask_used,sum,m2,n2)
        img3= mask.apply_mask(img_s_p, mask_used2,sum2,m22,n22)
        print(img)
        print("EMPTY SPACE")
        img4= sobel_edge.apply_sobel_edge(img)

        
        print(img3)

        cv2.imshow("Original",img)
        cv2.imshow("Noise Gaus",img_noise)
        cv2.imshow("Noise SP",img_s_p)
        cv2.imshow("Gaus",img2)        
        cv2.imshow("Unweighted",img3) 
        cv2.imshow("Soble Edge",img4) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()            

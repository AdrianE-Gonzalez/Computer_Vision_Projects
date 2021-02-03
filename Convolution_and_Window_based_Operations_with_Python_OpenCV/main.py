import cv2
import math 
import load_image

import convolution
import sobel_edge
import median_filtering
import noise
import mask

def run_test():
        for x in [1]:
        images=load_image.open_multiple_images(x)

        for img in images.values():
                
                img_noise=noise.add_gaussian_noise(50,100,img)
                img_s_p=noise.add_saltpepper_noise(img)

                # CONVOLUTION ALGORITHM
                # Creates Masks
                mask_1,sum_1,m2_1,n2_1= convolution.create_unweighted(mask_size=5) 
                mask_2,sum_2,m2_2,n2_2= convolution.create_weighted(mask_size=5) 
                mask_3,sum_3,m2_3,n2_3= convolution.create_gaussian(mask_size=5,sigma=1)
                
                # Applies Mask To Image
                unweighted= mask.apply_mask(img_s_p, mask_1,sum_1,m2_1,n2_1)
                weighted= mask.apply_mask(img_s_p, mask_2,sum_2,m2_2,n2_2)
                gaussian= mask.apply_mask(img_s_p, mask_3,sum_3,m2_3,n2_3)

                #MEDIAN FILTERING
                median= median_filtering.apply_median_filter(3,img_s_p)

                # SOBEL FILTERING
                sobel= sobel_edge.apply_sobel_edge(img)

                cv2.imshow("Original",img)
                cv2.imshow("Noise Gaus",img_noise)
                cv2.imshow("Noise SP",img_s_p)
                cv2.imshow("Unweighted",unweighted)        
                cv2.imshow("Weighted",weighted) 
                cv2.imshow("Gaussian",gaussian) 
                cv2.imshow("Median",median) 
                cv2.imshow("Sobel",sobel) 

                cv2.waitKey(0)
                cv2.destroyAllWindows()            

run_test()
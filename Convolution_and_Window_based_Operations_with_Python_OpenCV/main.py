import cv2
import math 
import load_image

from dotenv import load_dotenv
import os

import convolution
import sobel_edge
import median_filtering
import noise
import mask


# Runs Test For The Number Of Images Given In num_run
# Saves Image Results To Results Folder
# Uncomment imshow If You Want To View All Images Results
def run_test(num_run):
        
        load_dotenv()
        SAVE_PATH = os.getenv('SAVE_PATH')
        My_Filters = SAVE_PATH+'/My_Filters'
        OpenCV_Filters= SAVE_PATH+'/OpenCV_Filters'\
        
        for x in [num_run]:
                images=load_image.open_multiple_images(x)
                count=0
                # Loops Through All Images Selected In Load_Images
                for img in images.values():
                        count+=1
                        # Stores Original Image To Results Folder
                        temp_filename=My_Filters+'/Original/Original_'+str(count)+'.jpg'
                        temp_openCV_filename=OpenCV_Filters+'/Original/Original_'+str(count)+'.jpg'
                        cv2.imwrite(temp_filename, img)
                        cv2.imwrite(temp_openCV_filename, img) 
                        
                        # Variable To Store Both Image Noises
                        img_noise=[]

                        # Applies Noise Provided In The Project Instructions
                        img_gaus=noise.add_gaussian_noise(50,100,img)
                        img_s_p=noise.add_saltpepper_noise(img)
                        
                        # Stores Gaussian Noise Image To Results Folder
                        temp_filename=My_Filters+'/Gaussian_Noise/Gaussian_Noise_'+str(count)+'.jpg'
                        cv2.imwrite(temp_filename, img_gaus) 

                        # Stores Salt And Pepper Noise Image To Results Folder
                        temp_filename=My_Filters+'/Salt_And_Pepper_Noise/Salt_And_Pepper_Noise_'+str(count)+'.jpg'
                        cv2.imwrite(temp_filename, img_s_p) 

                        # Store Image Noises
                        img_noise.append((img_gaus,"Gaussian_Noise"))
                        img_noise.append((img_s_p,"Salt_And_Pepper_Noise"))
                        
                        # cv2.imshow("Original",img)
                        # cv2.imshow("Noise Gaus",img_gaus)
                        # cv2.imshow("Noise SP",img_s_p)

                        # Loops Through Both Gaussian Noise And Salt And Pepper Noise; Filters Images
                        for img_n in img_noise:
                                if img_n[1]=='Gaussian_Noise':
                                        # Changes Results Path To Gaussian_Filter
                                        filename=My_Filters+'/Gaussian_Filter/'
                                if img_n[1]=='Salt_And_Pepper_Noise':
                                        # Changes Results Path To Salt_And_Pepper_Filter
                                        filename=My_Filters+'/Salt_And_Pepper_Filter/'

                                # Loops For A 3x3 Mask And A 5x5 Mask
                                for matrix_ in [3,5]:

                                        if matrix_==3:
                                                # Changes Results Path To Gaussian_Filter
                                                filename_=filename+'/3x3_Mask/'
                                        if matrix_==5:
                                                # Changes Results Path To Salt_And_Pepper_Filter
                                                filename_=filename+'/5x5_Mask/'

                                        # CONVOLUTION ALGORITHM
                                        # Creates Masks
                                        mask_1,sum_1,m2_1,n2_1= convolution.create_unweighted(mask_size=5) 
                                        mask_2,sum_2,m2_2,n2_2= convolution.create_weighted(mask_size=5) 
                                        mask_3,sum_3,m2_3,n2_3= convolution.create_gaussian(mask_size=5,sigma=1)
                                        
                                        # Applies Mask To Image
                                        unweighted= mask.apply_mask(img_n[0], mask_1,sum_1,m2_1,n2_1)
                                        weighted= mask.apply_mask(img_n[0], mask_2,sum_2,m2_2,n2_2)
                                        gaussian= mask.apply_mask(img_n[0], mask_3,sum_3,m2_3,n2_3)
                                        
                                        # Stores unweighted Image To Results Folder
                                        temp_filename=filename_+'/Unweighted/Unweighted_Average_'+str(matrix_)+'x'+str(matrix_)+'_'+str(count)+'.jpg'
                                        cv2.imwrite(temp_filename, unweighted) 
                                        
                                        # Stores weighted Image To Results Folder
                                        temp_filename=filename_+'/Weighted/Weighted_Average_'+str(matrix_)+'x'+str(matrix_)+'_'+str(count)+'.jpg'
                                        cv2.imwrite(temp_filename, weighted) 
                                        
                                        # Stores gaussian Image To Results Folder
                                        temp_filename=filename_+'/Gaussian/Gaussian_Mask_'+str(matrix_)+'x'+str(matrix_)+'_'+str(count)+'.jpg'
                                        cv2.imwrite(temp_filename, gaussian) 
                                        
                                        #MEDIAN FILTERING
                                        median= median_filtering.apply_median_filter(5,img_n[0])

                                        # Stores median Image To Results Folder
                                        temp_filename=filename_+'/Median/Median_Filtering_'+str(matrix_)+'x'+str(matrix_)+'_'+str(count)+'.jpg'
                                        cv2.imwrite(temp_filename, median) 

                                        # cv2.imshow("Unweighted Average Of "+img_n[1],unweighted)        
                                        # cv2.imshow("Weighted Average Of "+img_n[1],weighted) 
                                        # cv2.imshow("Gaussian Mask Of "+img_n[1],gaussian) 
                                        # cv2.imshow("Median Filtering Of "+img_n[1],median) 

                        # SOBEL FILTERING
                        sobel= sobel_edge.apply_sobel_edge(img)

                        # Stores Sobel_Edge Image To Results Folder
                        temp_filename=My_Filters+'/Sobel_Edge/Sobel_Edge_'+str(count)+'.jpg'
                        cv2.imwrite(temp_filename, sobel) 

                        # cv2.imshow("Sobel",sobel) 
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()      


print("Running Test")
run_test(num_run=3)

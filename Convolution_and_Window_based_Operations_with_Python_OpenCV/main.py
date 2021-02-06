import cv2
import math 

from dotenv import load_dotenv
import os

import load_image
import convolution
import median_filtering
import sobel_edge
import noise
import mask
import openCV_mask_filters


# Runs Test For The Number Of Images Given In num_run
# Saves Image Results To Results Folder
# Uncomment imshow If You Want To View All Images Results
def run_test(num_run):
        
        load_dotenv()
        SAVE_PATH = os.getenv('SAVE_PATH')
        My_Filters = SAVE_PATH+'/My_Filters'
        OpenCV_Filters= SAVE_PATH+'/OpenCV_Filters'
        
        for x in [num_run]:
                images=load_image.open_multiple_images(x)
                count=0
                # Loops Through All Images Selected In Load_Images
                for img in images.values():
                        count+=1
                        # Stores Original Image To Results Folder
                        temp_filename=SAVE_PATH+'/Original/Original_'+str(count)+'.jpg'
                        cv2.imwrite(temp_filename, img)
                        
                        # Variable To Store Both Image Noises
                        img_noise=[]

                        # Applies Noise Provided In The Project Instructions
                        img_gaus=noise.add_gaussian_noise(50,100,img)
                        img_s_p=noise.add_saltpepper_noise(img)
                        
                        # Stores Gaussian Noise Image To Results Folder
                        temp_filename=SAVE_PATH+'/Gaussian_Noise/Gaussian_Noise_'+str(count)+'.jpg'
                        cv2.imwrite(temp_filename, img_gaus) 

                        # Stores Salt And Pepper Noise Image To Results Folder
                        temp_filename=SAVE_PATH+'/Salt_And_Pepper_Noise/Salt_And_Pepper_Noise_'+str(count)+'.jpg'
                        cv2.imwrite(temp_filename, img_s_p) 

                        # Store Image Noises In List By Tuples
                        # Use Tuple To Check String Which Noise Type 
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
                                        openCV_filename=OpenCV_Filters+'/Gaussian_Filter/'

                                if img_n[1]=='Salt_And_Pepper_Noise':
                                        # Changes Results Path To Salt_And_Pepper_Filter
                                        filename=My_Filters+'/Salt_And_Pepper_Filter/'
                                        openCV_filename=OpenCV_Filters+'/Salt_And_Pepper_Filter/'

                                # Loops For A 3x3 Mask And A 5x5 Mask
                                for matrix_ in [3,5]:

                                        if matrix_==3:
                                                # Changes Results Path To 3x3 Matrix
                                                filename_=filename+'/3x3_Mask/'
                                                openCV_filename_=openCV_filename+'/3x3_Mask/'

                                        if matrix_==5:
                                                # Changes Results Path To 5x5 Matrix
                                                filename_=filename+'/5x5_Mask/'
                                                openCV_filename_=openCV_filename+'/5x5_Mask/'

                                        # CONVOLUTION ALGORITHM
                                        # Creates Masks
                                        mask_1,sum_1,m2_1,n2_1= convolution.create_unweighted(mask_size=matrix_) 
                                        mask_2,sum_2,m2_2,n2_2= convolution.create_weighted(mask_size=matrix_) 
                                        mask_3,sum_3,m2_3,n2_3= convolution.create_gaussian(mask_size=matrix_,sigma=1)
                                        
                                        # Applies Mask To Image
                                        unweighted= mask.apply_mask(img_n[0], mask_1,sum_1,m2_1,n2_1)
                                        weighted= mask.apply_mask(img_n[0], mask_2,sum_2,m2_2,n2_2)
                                        gaussian= mask.apply_mask(img_n[0], mask_3,sum_3,m2_3,n2_3)
                                        
                                        # Applies openCV Filters To Image
                                        openCV_unweighted= openCV_mask_filters.get_unweighted(img_n[0],mask_size=matrix_)
                                        openCV_gaussian=openCV_mask_filters.get_gauss(img_n[0],mask_size=matrix_,sigma=1)
                                        
                                        # Stores unweighted Image To Results Folder
                                        temp_filename=filename_+'/Unweighted/Unweighted_Average_'+str(matrix_)+'x'+str(matrix_)+'_'+str(count)+'.jpg'
                                        cv2.imwrite(temp_filename, unweighted)
                                        
                                        # Stores openCV_unweighted Image To Results Folder 
                                        temp_openCV_filename=openCV_filename_+'/Unweighted/openCV_Unweighted_Average_'+str(matrix_)+'x'+str(matrix_)+'_'+str(count)+'.jpg'
                                        cv2.imwrite(temp_openCV_filename, openCV_unweighted) 

                                        # Stores weighted Image To Results Folder
                                        temp_filename=filename_+'/Weighted/Weighted_Average_'+str(matrix_)+'x'+str(matrix_)+'_'+str(count)+'.jpg'
                                        cv2.imwrite(temp_filename, weighted) 
                                        
                                        # Stores gaussian Image To Results Folder
                                        temp_filename=filename_+'/Gaussian/Gaussian_Mask_'+str(matrix_)+'x'+str(matrix_)+'_'+str(count)+'.jpg'
                                        cv2.imwrite(temp_filename, gaussian) 
                                        
                                        # Stores openCV_gaussian Image To Results Folder
                                        temp_openCV_filename=openCV_filename_+'/Gaussian/openCV_Gaussian_Mask_'+str(matrix_)+'x'+str(matrix_)+'_'+str(count)+'.jpg'
                                        cv2.imwrite(temp_openCV_filename, openCV_gaussian) 
                                        
                                        #MEDIAN FILTERING
                                        median= median_filtering.apply_median_filter(matrix_,img_n[0])

                                        # Applies openCV Median Filter To Image
                                        openCV_median=openCV_mask_filters.get_median(img_n[0],mask_size=matrix_)

                                        # Stores median Image To Results Folder
                                        temp_filename=filename_+'/Median/Median_Filtering_'+str(matrix_)+'x'+str(matrix_)+'_'+str(count)+'.jpg'
                                        cv2.imwrite(temp_filename, median) 
                                        
                                        # Stores openCV_median Image To Results Folder
                                        temp_openCV_filename=openCV_filename_+'/Median/openCV_Median_Filtering_'+str(matrix_)+'x'+str(matrix_)+'_'+str(count)+'.jpg'
                                        cv2.imwrite(temp_openCV_filename, openCV_median) 
                                        
                                        # cv2.imshow("Unweighted Average Of "+img_n[1],unweighted)        
                                        # cv2.imshow("Weighted Average Of "+img_n[1],weighted) 
                                        # cv2.imshow("Gaussian Mask Of "+img_n[1],gaussian) 
                                        # cv2.imshow("Median Filtering Of "+img_n[1],median) 
                        
                        for num_ in [3,5]:
                                if num_==3:
                                        # Changes Results Path To 3x3 Matrix
                                        filename_=My_Filters+'/Sobel_Edge/3x3_Mask/'
                                        openCV_filename_=OpenCV_Filters+'/Sobel_Edge/3x3_Mask/'

                                if num_==5:
                                        # Changes Results Path To 5x5 Matrix
                                        filename_=My_Filters+'/Sobel_Edge/5x5_Mask/'
                                        openCV_filename_=OpenCV_Filters+'/Sobel_Edge/5x5_Mask/'

                                # SOBEL FILTERING
                                sobel= sobel_edge.get_sobel_mask(img,mask_size=num_)

                                # Applies openCV Sobel Filter To Image
                                openCV_sobel=openCV_mask_filters.get_sobel(img,mask_size=num_)

                                # Stores sobel Image To Results Folder
                                temp_filename=filename_+'Sobel_Edge_'+str(num_)+'x'+str(num_)+'_'+str(count)+'.jpg'
                                cv2.imwrite(temp_filename, sobel) 
                                
                                # Stores openCV_sobel Image To Results Folder
                                temp_openCV_filename=openCV_filename_+'openCV_Sobel_Edge_'+str(num_)+'x'+str(num_)+'_'+str(count)+'.jpg'
                                cv2.imwrite(temp_openCV_filename, openCV_sobel)

                        # SOBEL FILTERING
                        sobel= sobel_edge.apply_sobel_edge(img)

                        # Applies openCV Sobel Filter To Image
                        openCV_sobel=openCV_mask_filters.get_sobel(img,mask_size=1)

                        # Stores sobel Image To Results Folder
                        temp_filename=My_Filters+'/Sobel_Edge/Sobel_Edge_'+str(count)+'.jpg'
                        cv2.imwrite(temp_filename, sobel) 
                        
                        # Stores openCV_sobel Image To Results Folder
                        temp_openCV_filename=OpenCV_Filters+'/Sobel_Edge/openCV_Sobel_Edge_'+str(count)+'.jpg'
                        cv2.imwrite(temp_openCV_filename, openCV_sobel) 
                        
                        # cv2.imshow("Sobel",sobel) 
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()      

def run_openCV_test(num_run):

        for x in [num_run]:
                images=load_image.open_multiple_images(x)
                count=0
                # Loops Through All Images Selected In Load_Images
                for img in images.values():
                        img_gaus=noise.add_gaussian_noise(50,100,img)
                        img_s_p=noise.add_saltpepper_noise(img)

                        openCV_unweighted= openCV_mask_filters.get_unweighted(img_s_p,mask_size=5)
                        openCV_gauss=openCV_mask_filters.get_gauss(img_s_p,mask_size=5,sigma=1)
                        openCV_median=openCV_mask_filters.get_median(img_s_p,mask_size=5)
                        openCV_sobel=openCV_mask_filters.get_sobel(img,mask_size=3)
                        sobel=sobel_edge.get_sobel_mask(img,mask_size=3)


                        # cv2.imshow("Original",img) 
                        # cv2.imshow("Salt and Pepper Noise",img_s_p) 
                        # cv2.imshow("Gauss Noise",img_gaus) 
                        # cv2.imshow("Unwieghted",openCV_unweighted) 
                        # cv2.imshow("Gauss",openCV_gauss) 
                        # cv2.imshow("Median",openCV_median) 
                        # cv2.imshow("Sobel",openCV_sobel) 
                        # cv2.imshow("Sobel1",sobel) 

                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()   


# Test Runs OpenCV Filters For One Image
# Can Change num_run To The Amount Of Images Wanting To Test
print("Running Test")
run_test(num_run=3)

# Test Runs OpenCV Filters For One Image
# Can Change num_run To The Amount Of Images Wanting To Test
# print("Running openCV Test")
# run_openCV_test(num_run=1)

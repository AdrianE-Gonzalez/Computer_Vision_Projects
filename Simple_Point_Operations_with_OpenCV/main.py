# This is where the main code will run if any extra files are used


# Instructions

# - Change brightness without regard to position in the image.
# - These operations are memoryless: Don’t have to remember any other points except at (x,y).
#   This means that operations can be done in real time (the system is causal)
# - These operations, from a computation point of view, can be done in place (eventually replacing f by g) without requiring extra storage (another storage for g)
# - They work on one pixel at a time, i.e. a 1x1 neighborhood
# - They can be described either by a transformation equation or graphically by an input/output relationship. 
#               ▪ Graphically the x-axis represents the input gray level, and the y-axis represents the output gray level
#               ▪ A LUT (look up table) can be used to implement the relationship
#                   - Entries of the LUT would be calculated off-line
#                   - G[x][y]= LUT[ f[x][y] ]

#   1. Apply the three following point operations on a set of images of images. You should be able to find many sets of images on the internet. 
#      You will apply the point operations on the gray level version of the image in two ways: one with the formula given and one by creating the LUT for each operation. 
#       A. Thresholding:
#               g(x,y)={255 if f(x,y)>128 }
#                      {0   otherwise     }
#       B. Negative image:
#               g(x,y)={255-f(x,y)}
#       C. Log transform:
#               g(x,y)={c log10 (1+x)}
#   2. Time the two approaches (python some timing utilities such as timeit), and see if there is any difference for 1, 10, 20, 30, and 50 images. 
#      Create a word-document report with a table comparing the two approaches, similar to the following

import Threshholding
import Negative_Image
import Log_Transform
import Load_Images

from dotenv import load_dotenv
import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

import time
import sys

load_dotenv()
image_results_path = os.getenv('SAVE_PATH')
image_results_path=image_results_path+"/"+"image_times.txt"
# Tests a Single Grayscale Image Using Threshhold, Negative, and Log Transform
# This Code Was My First Attempt To Figuring Out Where I Wanted To Take This Project
# This Code Can Be Ignored Considering You Can Get One Random Image From test_multiple_images() Function
def test_single_image():
        
    # Loads Single Static Image
    image=Load_Images.open_single_image()


    # Uses ThreshHold On Grayscale Image
    thresh_image=Threshholding.threshhold_image(image)
    thresh_image_LUT=Threshholding.threshhold_image_LUT(image)
    # Uses Negative On Grayscale Image
    negative_image=Negative_Image.negative_image(image)
    negative_image_LUT=Negative_Image.negative_image_LUT(image)
    # Uses Log Transform On Grayscale Image
    log_transform_image=Log_Transform.log_transform_image(image)
    log_transform_image_LUT=Log_Transform.log_transform_image_LUT(image)
    # Shows All Images: Grayscale, Threshhold, Negative, and Log Transform


    cv2.imshow("BGR to Gray Image", image)
    cv2.imshow("Threshholding Image", thresh_image)
    cv2.imshow("LUT Threshholding Image", thresh_image_LUT)
    cv2.imshow("Negative Image", negative_image)
    cv2.imshow("LUT Negative Image", negative_image_LUT)
    cv2.imshow("Log Transform Image", log_transform_image)
    cv2.imshow("LUT Log Transform Image", log_transform_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Calls How Many Images To Get From Testing Images
# Filters Each Image To Either thresh_image, negative_image or log_transform_image, Using Formula, Pixel By Pixel Formula, Or LUT
# Saves Image Filters In Results Folder
# Saves Run Times In Results Folder
def test_multiple_images(num):
    #Loads The Amount Of Images Given
    images = Load_Images.open_multiple_images(num)

    # Created A Dictionary Of All Filters Being Used And Stores A Tuple Of Each Dictionary Of Images That Was Created And The Time It Took To Convert All The Images Stored In The Dictionary Of Images
    #
    # Key: Image Filters
    # Value: Tuple(Dictionary Of Images, Time It Took To Convert Original To Filter)
    image_operation={
            'original_image':(dict(images),0),
            'thresh_image':(dict(images),0),
            'thresh_image_Loop':(dict(images),0),
            'thresh_image_LUT':(dict(images),0),
            'negative_image':(dict(images),0),
            'negative_image_Loop':(dict(images),0),
            'negative_image_LUT':(dict(images),0),
            'log_transform_image':(dict(images),0),
            'log_transform_image_Loop':(dict(images),0),
            'log_transform_image_LUT':(dict(images),0),
    }
    
    # Iterates Through image_operation Dictionary, In Order To Loop Through Each Image Filter
    # I Did It Like This In Order To Help When Timing How Long Each Convertion Takes
    for img in image_operation:
        # Created temp_tuple To Temporarly Store The Tuple Stored In The Dictionary And Convert It To A List In Order To Edit The Tuple
        # I Did This Because You Cannot Change A Tuple Once Stored Inside A Dictionary
        temp_tuple = list(image_operation[img])
        start_time = time.time()
        
        for image in temp_tuple[0].keys():
            if img == 'original_image':
                continue
            elif img == 'thresh_image':
                temp_tuple[0][image]=Threshholding.threshhold_image(temp_tuple[0][image],False)
            elif img == 'thresh_image_Loop':
                temp_tuple[0][image]=Threshholding.threshhold_image(temp_tuple[0][image],True)
            elif img == 'thresh_image_LUT':
                temp_tuple[0][image]=Threshholding.threshhold_image_LUT(temp_tuple[0][image])
            elif img == 'negative_image':
                temp_tuple[0][image]=Negative_Image.negative_image(temp_tuple[0][image],False)
            elif img == 'negative_image_Loop':
                temp_tuple[0][image]=Negative_Image.negative_image(temp_tuple[0][image],True)
            elif img == 'negative_image_LUT':
                temp_tuple[0][image]=Negative_Image.negative_image_LUT(temp_tuple[0][image])
            elif img == 'log_transform_image':
                temp_tuple[0][image]=Log_Transform.log_transform_image(temp_tuple[0][image],False)
            elif img == 'log_transform_image_Loop':
                temp_tuple[0][image]=Log_Transform.log_transform_image(temp_tuple[0][image],True)
            elif img == 'log_transform_image_LUT':
                temp_tuple[0][image]=Log_Transform.log_transform_image_LUT(temp_tuple[0][image])
            else:
                continue

        end_time = time.time()
        temp_tuple[1] = end_time-start_time
        image_operation[img] = tuple(temp_tuple)
        
    # Loops Through Each Dictionary Of Images And Only Prints Out One Timer (Time That Was Calculated)
    # Uncomment cv2 To See Images One By One
    load_dotenv()
    filename= os.getenv('SAVE_PATH')
    with open(image_results_path, 'a') as f:
        print("",file=f)
    
    for i in image_operation:
        count=1
        for j in image_operation[i][0].values():
            # Only Saves Images Which Test Run == 10 Images
            if num == 10:
                temp_filename=filename+'/'+i
                temp_filename=temp_filename+('/'+i+'_'+str(count))+'.jpg'
                count=count+1
                cv2.imwrite(temp_filename, j) 
                #print('NAME:: '+temp_filename)
                #cv2.imshow(i, j)
                #cv2.waitKey(0)
                #cv2.destroyAllWindows()            
            continue
        with open(image_results_path, 'a') as f:
            print('{:<20}{:<35}{:<20}'.format(str(num),i,str(image_operation[i][1])), file=f)

# Tests a Single Specified Image,
# This Code Can Be Ignored Considering You Can Get One Random Image From test_multiple_images() Function
#test_single_image()


# If You Don't Remove The File, It Will Add On To Existing Test Runs
# If You Don't Have A TXT File Name image_times.txt, The Code Won't Run!!!!!!!!!!!!!!!!!!!
os.remove(image_results_path)
# Names Each Column In image_times.txt
with open(image_results_path, 'a') as f:
        print('{:<20}{:<35}{:<20}'.format('No Of Images','Filename','RunTimes'),file=f)
# Loops Through Each Iteration [1,10,20,30,50]
for x in [1,10,20,30,50]:
    print("TESTING "+str(x)+( " IMAGE"if x==1 else " IMAGES"))
    test_multiple_images(x)
    print()




# I wanted to show all images in a single window display using plt
# but plt has issues in arch-linux because of cv2

# Code Used To Show All Images In A Single Window Display
# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax1.set_title("BGR to Gray Image")
# ax1.imshow(image)

# fig.add_subplot(2,2,2)
# ax2.set_title("Threshholding Image")
# ax2.imshow(thresh_image)

# fig.add_subplot(2,2,3)
# ax3.set_title("Negative Image")
# ax3.imshow(negative_image)

# #fig.add_subplot(2,2,4)
# ax4.set_title("Log Transform Image")
# ax4.imshow(log_transform_image)
# plt.show()
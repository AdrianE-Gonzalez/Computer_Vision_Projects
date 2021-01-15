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

import cv2
import numpy as np
import matplotlib.pyplot as plt


# Tests a Single Image Using Grayscale, Threshhold, Negative, and Log Transform
def test_single_image():
        
    # Loads Single Static Image
    image=Load_Images.open_single_image()


    # Uses ThreshHold On Grayscale Image
    thresh_image=Threshholding.threshhold_image(image)
    # Uses Negative On Grayscale Image
    negative_image=Negative_Image.negative_image(image)
    # Uses Log Transform On Grayscale Image
    log_transform_image=Log_Transform.log_transform_image(image)
    # Shows All Images: Grayscale, Threshhold, Negative, and Log Transform


    cv2.imshow("BGR to Gray Image", image)
    cv2.imshow("Threshholding Image", thresh_image)
    cv2.imshow("Negative Image", negative_image)
    cv2.imshow("Log Transform Image", log_transform_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_multiple_images():
    images = Load_Images.open_multiple_images(1)

    for img in images:
        # Uses ThreshHold On Grayscale Image
        thresh_image=Threshholding.threshhold_image(img)
        # Uses Negative On Grayscale Image
        negative_image=Negative_Image.negative_image(img)
        # Uses Log Transform On Grayscale Image
        log_transform_image=Log_Transform.log_transform_image(img)

        # Shows All Images: Grayscale, Threshhold, Negative, and Log Transform
        cv2.imshow("BGR to Gray Image", img)
        cv2.imshow("Threshholding Image", thresh_image)
        cv2.imshow("Negative Image", negative_image)
        cv2.imshow("Log Transform Image", log_transform_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
   

# Tests a Single Image
# test_single_image()

# Tests The Amount of Image User Sets
# test_multiple_images()




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



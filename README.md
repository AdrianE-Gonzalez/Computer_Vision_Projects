5 python files and 1 .env file
=============
Python files include: Load_Images, Log_Transform, Negative_Image,Threshholding, and main
=============
Load_Images.py:
-------------

1. Imports used: cv2, random, os, glob, load_env
   - cv2: used to read images and used to convert images to grayscale
   - random: used to select a random image from the Images folder
   - os: Used to get file paths from the .env file
   - glob: Used to get each image from the Image Folder
   - load_env: used to load .env file
1. contains 2 functions:
   - open_single_image():
     - loads a single specified image from the Image Folder
   - open_multiple_images(image_amount):
     - image_amount: The number given from the list ([1,10,20,30,50])
     - load a random list of images from the Image Folder based on the image_amount given

Log_Transform.py
-------------
1. Imports used: cv2, numpy
1. contains 3 functions:
   - log_transform_image(image,looping): contains 2 functions
     - image= the image being passed through
     - looping= boolean opperations stating whether to use the formula for the full image or for every pixel
     - formula():
       - computes the image to the given formula
     - looping_formula():
       - computes each pixel to the given formula
   - create_lut_log_transform():
     - creates the lut table for log transform
   - log_transform_image_LUT(image):
     - image= the image being passed through
     - computes each pixel given the LUT

Negative_Image.py
-------------
1. Imports used: cv2, numpy
1. contains 3 functions:
   - negative_image(image,looping): contains 2 functions
     - image= the image being passed through
     - looping= boolean opperations stating whether to use the formula for the full image or for every pixel
     - formula():
       - computes the image to the given formula
     - looping_formula():
       - computes each pixel to the given formula
   - create_lut_negative():
     - creates the lut table for negative
   - negative_image_LUT(image):
     - image= the image being passed through
     - computes each pixel given the LUT

Threshholding.py
-------------
1. Imports used: cv2, numpy
1. contains 2 functions:
   - threshhold_image(image,looping): contains 2 functions
     - image= the image being passed through
     - looping= boolean opperations stating whether to use the formula for the full image or for every pixel
     - formula():
       - computes the image to the given formula
     - looping_formula():
       - computes each pixel to the given formula
   - create_lut_threshhold():
     - creates the lut table for thresholding
   - threshhold_image_LUT(image):
     - image= the image being passed through
     - computes each pixel given the LUT



main.py
-------------
*When you run main.py, it will go through [1,10,20,30,50] images using the test_multiple_images(num) function and store the results in Results Folder 
1. Imports Used: 
   - Python Files Created: Threshholding, Negative_Image, Log_Transform, and Load_Images
   - Imports used to load SAVE_PATH: load_dotenv and os
     - Helps store images to respective folders in results, and saves times in txt file
   - Other Imports: cv2, numpy, and matplotlib.pyplot
   - imports used to time each amount of images: time and sys
1. Contains 2 functions:
   - test_single_image()
     - Test a single specified image and converts them to all the operations, also displays them using cv2.imgshow 
   - test_multiple_images(num)
     - Test multiple images specified by parameter ‘num’ and stores images in their respective folder when num=10, and records run times in txt file and stores them in results folder

Results Folder Contains Changed Images and times recorded from latest test runs.
Results Folder also contains tables from test results and screenshots from runs.

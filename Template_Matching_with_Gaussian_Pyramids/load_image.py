# Import Used To Read Images
import cv2

#Import Used To Select Random Image
import random

# Imports Used To Load Images
import os
import glob
from dotenv import load_dotenv

def load_images(img_num):

    # Gets FILE_PATH From Environment File
    load_dotenv()
    FILE_PATH= os.getenv('FILE_PATH')

    # Initialize List
    img_list= []
    rand_list= []

    # Stores All The ImagesTo img_list From The Folder's FILE_PATH And Converts Images From Color To Grayscale, 
    for x in glob.glob(FILE_PATH+'/*.png'):
        
        img_list.append(cv2.cvtColor(cv2.imread(x),cv2.COLOR_BGR2GRAY))

    # Stores A Random Image From img_list To rand_list
    for x in range(img_num):
        # Select A Random Image From img_list
        temp= random.choice(img_list)
        # Appends Selected Image To rand_list
        rand_list.append(temp)

    return rand_list
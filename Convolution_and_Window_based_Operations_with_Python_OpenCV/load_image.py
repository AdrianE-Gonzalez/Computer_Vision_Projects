import cv2
import random
import os
import glob
from dotenv import load_dotenv


# Returns A List Of Random Grayscale Images, Based On The image_amount
def open_multiple_images(image_amount):
    #This is Used To Access Images In Specified File Path
    load_dotenv()
    FILE_PATH = os.getenv('FILE_PATH')
    
    #List Variables
    image_list= []
    random_images_list= {}

    # Loops Through The Folder Containing The Images Ending In .png
    # Appends Each Image To image_list
    #       -Inside The Append It Converts The Read Image From BGR To Grayscale
    #               -Inside The cvtColor, It Reads A Single Image From FILE_PATH
    for p in glob.glob(FILE_PATH+"/*.png"):
        image_list.append(cv2.cvtColor(cv2.imread(p), cv2.COLOR_BGR2GRAY))

    # Loops Based On The image_amount
    for x in range(image_amount):
        #Picks A Random Image On image_list And Stores It In temp
        temp=random.choice(image_list)
        #Appends The Image Stored In temp And Appends It To random_images_list
        random_images_list[x]=temp
    
    return random_images_list
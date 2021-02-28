from load_image import load_images
import pyramid as pyd 
import cv2
import random
import diagonal_image as di
import numpy as np

import os
from dotenv import load_dotenv

def test_run(num_run):
    load_dotenv()
    SAVE_PATH= os.getenv("SAVE_PATH")

    # Images Size 384,384
    img=load_images(num_run)
    metric_list= ['ncc','nssd']
    cnt=0

    for i in img:

        cnt=cnt+1
        M,N=i.shape
        rand= random.randint(0, M-32)
        template_image= i[rand:rand+32,rand:rand+32]

        #ix= m.get_normalized_ssd(down_2, up_2)
        for metric in metric_list:
            # image, template, no_of_levels, metric
            imgs, temps, xx= pyd.pyramid_temp_match(i, template_image,3,metric)
            
            original_image= di.get_diagonal(imgs)
            templ_image= di.get_diagonal(temps)
            di_image= di.get_diagonal(xx)

            cv2.imwrite((SAVE_PATH+'/Original/Original_Image_'+str(cnt)+'.png'),original_image)
            cv2.imwrite((SAVE_PATH+'/Template_Image/Template_Image_'+str(cnt)+'.png'),templ_image)
            if metric == 'ncc':
                cv2.imwrite((SAVE_PATH+'/Normalized_Cross_Correlation/NCC_Image_'+str(cnt)+'.png'),di_image)
            else:
                cv2.imwrite((SAVE_PATH+'/Normalized_SSD/NSSD_Image_'+str(cnt)+'.png'),di_image)

            # cv2.imshow('Original_Image',original_image)
            # cv2.imshow('Template_Image',templ_image)
            # cv2.imshow('NSSD_Image',di_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            
        # for nu in range(0,3):
        #     k,l= temps[nu].shape
        #     temps[nu]= cv2.resize(temps[nu],(k*12,l*12))
            
        #     cv2.imshow(('Original_Image_'+str(imgs[nu].shape)),imgs[nu])
        #     cv2.imshow(('Template_Image_'+str(k)+','+str(l)),temps[nu])
        #     cv2.imshow(('SSD_Image_'+str(xx[nu].shape)),xx[nu])
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()

def test_run_single(num_run):

    load_dotenv()
    SAVE_PATH= os.getenv("SAVE_PATH")

    # Images Size 384,384
    img=load_images(1)
    metric_list= ['nssd']
    cnt=0

    for i in img:
        cnt=cnt+1
        M,N=i.shape
        rand= random.randint(0, M-32)
        template_image= i[rand:rand+32,rand:rand+32]
        print('rand: '+str(rand))
        #ix= m.get_normalized_ssd(down_2, up_2)
        for metric in metric_list:
            # image, template, no_of_levels, metric
            imgs, temps, xx= pyd.correlation(i, template_image,num_run,metric)
            
            print()
            print(i)
            print()
            print(template_image)
            cv2.imshow(('Original_Image_'),i)
            cv2.imshow(('Template_Image_'),template_image)
            cv2.imshow(('SSD_Image_'),xx[0])
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# Used to speed up the testing process with a specific problem. In order to make sure the calculations were correct.
def test_():
    image= np.array([[1, 3, 2, 5, 8, 9],
                        [2, 4, 6, 8, 9, 9],
                        [7, 6, 4, 8, 9, 6],
                        [1, 4, 6, 7, 3, 9],
                        [6, 4, 7, 9, 6, 4],
                        [8, 6, 4, 6, 8, 9]])
    template_image=np.array([[9, 6],
                            [3, 9]])

    imgs, temps, xx= pyd.correlation(image, template_image,1,'nssd')
    print('image')
    print(image)
    print('YIKERS')
    print(template_image)
    print("SUPPERS")
    print(xx[0])

# test_()
# test_run_single(3)
test_run(3)
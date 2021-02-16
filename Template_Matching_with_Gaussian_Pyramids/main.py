from load_image import load_images
import pyramid as pyd 
import cv2
import random
import diagonal_image as di

import os
from dotenv import load_dotenv

def test_run():
    load_dotenv()
    SAVE_PATH= os.getenv("SAVE_PATH")

    # Images Size 384,384
    img=load_images(1)
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

test_run()
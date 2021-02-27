# Created Python Files
import numpy as np
import cv2
import math
import metric as met

# sumation(u,v) (I-1(u,v)-)
def pyramid_temp_match(image, template, no_of_levels, metric):

    image_list= []
    image_list.append(image)

    temp_list=[]
    temp_list.append(template)

    temp_match_list=[]
    temp_cal=0

    m,n=0,0

    # Resize input image to pow of 2
    for num in range(0,no_of_levels-1):
        image_list.append(pyr_down(image_list[num]))
        temp_list.append(pyr_down(temp_list[num]))
    
    for num in range(0,no_of_levels):    
        temp_match=image_list[num].copy()
        m,n= temp_list[num].shape

        if metric == 'ncc':
            temp_cal= cv2.matchTemplate(image_list[num], temp_list[num],cv2.TM_CCORR_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(temp_cal)
            top_left= max_loc

        elif metric == 'nssd':
            temp_cal= cv2.matchTemplate(image_list[num], temp_list[num],cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(temp_cal)
            top_left= max_loc
    
        
        bottom_right = (top_left[0] + m, top_left[1] + n)

        for x in range(top_left[0],bottom_right[0]):
            for y in range(top_left[1],bottom_right[1]):
                temp_match[x][y]=np.uint8(255)

        temp_match_list.append(temp_match)
    return image_list, temp_list, temp_match_list


# Returns pyr_down_img
# Creates A Lower Resolution Of The image
def pyr_down(image):

    pyr_down_img= cv2.pyrDown(image)

    return pyr_down_img
def pyr_up(image):

    pyr_up_img= cv2.pyrUp(image)

    return pyr_up_img

# Used To Run A Temp_Matching Using Formulas    
def correlation(image, template, no_of_levels, metric):

    M,N= image.shape

    image_list= []
    image_list.append(image)

    temp_list=[]
    temp_list.append(template)

    temp_match_list=[]
    temp_cal=0

    m,n=0,0

    # Resize input image to pow of 2
    for num in range(0,no_of_levels-1):
        image_list.append(pyr_down(image_list[num]))
        temp_list.append(pyr_down(temp_list[num]))
    
    for num in range(0,no_of_levels):    
        temp_match=image_list[num].copy()
        m,n= temp_list[num].shape
        top_left=(0,0)
        if metric == 'ncc':
            temp_cal=met.get_normalized_cross_correlation(image_list[num], temp_list[num])
            #top_left= max_loc

        elif metric == 'nssd':
            temp_cal= met.get_normalized_ssd(image_list[num], temp_list[num])

            for x in range(0,M):
                for y in range(0,N):
                    if template[0][0]==temp_cal[x][y]:
                        top_left= (x,y)
                        print(top_left)
                        break
                else:
                    continue
                break

   
        bottom_right = (top_left[0] + m, top_left[1] + n)

        temp_match_list.append(temp_match)
    return image_list, temp_list, temp_match_list

    # l= math.log10(n/m)

    # ref_window= m*m
    # input_window= math.pow(2*m,2)

    # # Find Best Match Of ref_window in the input_window

    # input_window= math.pow(2*m,2)

import numpy as np
import math

def get_normalized_cross_correlation(image, template_image):
    # ?
    cross_corr= 0
    sum= 0
    M,N= image.shape
    m,n= template_image.shape

    
    template_dict={}
    template_div_dict={}
    img_mean_dict={}

    # Loops Through Image
    for x in range(m, M-m):
        for y in range(n, N-n):
            # Loops Through Template
            for u in range(-m, m):
                for v in range(-n, n):

                    

                    # Checks If Coordinates Are In The img_mean_dict
                    if not((x,y) in img_mean_dict):
                        img_mean_dict[(x,y)]=get_mean(image,template_image,x,y)
                    
                    # Section Of Template In Original Image Minus The Mean Of The Section Of Template In Original Image
                    image_cal= image[x+u][y+v]-img_mean_dict[(x,y)]

                    if not(template_image[u][v] in template_dict):
                        # Template Minus The Mean Of Template
                        template_cal= (template_image[u][v]-np.mean(template_image))
                        template_dict[template_image[u][v]]= template_cal


                    cross= image_cal*template_dict[template_image[u][v]]
                    norm= math.sqrt((image_cal**2)*(template_dict[template_image[u][v]]**2))

                    cross_norm= cross/norm
        print('X='+str(x))
    return cross_norm

def get_normalized_ssd(image, template_image):
    ssd= 0
    sum=0.0

    g=image.copy()
    
    M,N= image.shape
    m,n= template_image.shape
    
    template_dict={}
    img_mean_dict={}

    img_cal_dict={}
    cal_dict={}
    ssd_dict={}

    dictu={}
    # Loops Through Image
    for x in range(0, M):
        for y in range(0, N):
            sum=0.0
            # Loops Through Template
            for u in range(-m, m-1):
                for v in range(-n, n-1):
                                       
                    j=x+u
                    k=y+v

                     # Checks If Coordinates Are In The img_mean_dict
                    if not((x,y) in img_mean_dict):
                        img_mean_dict[(x,y)]=get_mean(image,template_image,x,y)
 
                    if not((image[j][k],img_mean_dict[(x,y)]) in cal_dict):
                        image_cal= image[j][k]-img_mean_dict[(x,y)]
                        cal_dict[image[j][k],img_mean_dict[(x,y)]]= image_cal

                    if not(template_image[u][v] in template_dict):
                        template_cal= template_image[u][v]-np.mean(template_image)
                        template_div= template_cal/(np.sqrt((template_cal**2)))
                        template_dict[template_image[u][v]]= template_div
                    
                    if not(cal_dict[image[j][k],img_mean_dict[(x,y)]] in img_cal_dict):
                        num_div=cal_dict[image[j][k],img_mean_dict[(x,y)]]
                        din_div=(np.sqrt((cal_dict[image[j][k],img_mean_dict[(x,y)]]**2)))
                        image_div= (0 if (din_div==0) else num_div/din_div)
                        img_cal_dict[cal_dict[image[j][k],img_mean_dict[(x,y)]]]=image_div
                    
                    if not((img_cal_dict[cal_dict[image[j][k],img_mean_dict[(x,y)]]],template_dict[template_image[u][v]]) in ssd_dict):
                        ssd_norm= ((img_cal_dict[cal_dict[image[j][k],img_mean_dict[(x,y)]]]-template_dict[template_image[u][v]])**2)
                        ssd_dict[img_cal_dict[cal_dict[image[j][k],img_mean_dict[(x,y)]]],template_dict[template_image[u][v]]]=ssd_norm

                    print(ssd_dict[img_cal_dict[cal_dict[image[j][k],img_mean_dict[(x,y)]]],template_dict[template_image[u][v]]])
                    sum=ssd_dict[img_cal_dict[cal_dict[image[j][k],img_mean_dict[(x,y)]]],template_dict[template_image[u][v]]]+sum
            print(x)
            print(y)
            print(sum)
            print()
            g[x][y]=(sum).clip(0,255).astype(np.uint8)
    print('G')
    print(g)    
    return g

def get_mean(image,template,u,v):

    M,N= template.shape
    img_mean= image[u:u+M,v:v+M]
    img_mean= np.mean(img_mean)
    return img_mean


# def get_normalized_ssd(image, template_image):
#     ssd= 0
#     sum=0.0

#     g=image.copy()
    
#     M,N= image.shape
#     m,n= template_image.shape
    
#     template_dict={}
#     template_div_dict={}
#     img_mean_dict={}
#     # Loops Through Image
#     for x in range(m, M-m):
#         for y in range(n, N-n):
#             sum=0.0
#             # Loops Through Template
#             for u in range(-m, m):
#                 for v in range(-n, n):
#                     # Checks If Coordinates Are In The img_mean_dict
#                     if not((x,y) in img_mean_dict):
#                         img_mean_dict[(x,y)]=get_mean(image,template_image,x,y)
#                         print('means')
#                         print(get_mean(image,template_image,x,y))
#                         print('means')
#                     image_cal= image[x+u][y+v]-img_mean_dict[(x,y)]

#                     if not(template_image[u][v] in template_dict):
#                         template_cal= template_image[u][v]-np.mean(template_image)
#                         template_dict[template_image[u][v]]= template_cal

#                     image_div= image_cal/(math.sqrt(math.pow(image_cal,2)))

#                     if  not(template_image[u][v] in template_div_dict):
#                         template_div= template_dict[template_image[u][v]]/(math.sqrt(math.pow(template_dict[template_image[u][v]],2)))
#                         template_div_dict[template_image[u][v]]= template_div
                    
#                     ssd_norm= math.pow((image_div-template_div_dict[template_image[u][v]]),2)

#                     print(ssd_norm)
#                     sum=ssd_norm+sum
#             g[x][y]=np.uint8(sum)
    
#     return g
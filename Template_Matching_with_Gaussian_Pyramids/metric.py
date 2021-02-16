import numpy as np

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
            for u in range(0, m):
                for v in range(0, n):

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
                    norm= np.sqrt((image_cal**2)*(template_dict[template_image[u][v]]**2))

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
    template_div_dict={}
    img_mean_dict={}
    # Loops Through Image
    for x in range(m, M-m):
        for y in range(n, N-n):
            sum=0.0
            # Loops Through Template
            for u in range(-m, m):
                for v in range(-n, n):
                    # Checks If Coordinates Are In The img_mean_dict
                    if not((x,y) in img_mean_dict):
                        img_mean_dict[(x,y)]=get_mean(image,template_image,x,y)
                    
                    image_cal= image[x+u][y+v]-img_mean_dict[(x,y)]

                    if not(template_image[u][v] in template_dict):
                        template_cal= template_image[u][v]-np.mean(template_image)
                        template_dict[template_image[u][v]]= template_cal

                    image_div= image_cal/(np.sqrt(image_cal**2))

                    if  not(template_image[u][v] in template_div_dict):
                        template_div= template_dict[template_image[u][v]]/(np.sqrt(template_dict[template_image[u][v]]**2))
                        template_div_dict[template_image[u][v]]= template_div
                    
                    ssd_norm= (image_div-template_div_dict[template_image[u][v]])**2
                    sum=ssd_norm+sum
            g[x][y]=np.uint8(sum)
        print('X='+str(x))
    
    return g
def get_mean(image,template,u,v):

    M,N= template.shape
    img_mean= image[u:u+M-1,v:v+M-1]
    img_mean= np.mean(img_mean)
    return img_mean

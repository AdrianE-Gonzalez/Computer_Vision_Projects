import numpy as np

def add_gaussian_noise(mean,variance,image):
      row,col,ch= image.shape
      st_dev = math.sqrt(variance)
      gauss_noise = np.random.normal(mean,st_dev,(row,col,ch))
      gauss_noise = gauss_noise.reshape(row,col,ch)
      noisy = image + gauss_noise
      noisy = noisy.clip(0,255).astype(np.uint8)
      show_image(noisy)
      return noisy   

def add_saltpepper_noise(image,p=0.10, s_vs_p=0.50):
    row,col,ch = image.shape
    image_plus_noise = np.copy(image)
    
    # Salt mode
    num_salt = np.ceil(p * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    image_plus_noise[coords] = 255
    
    # Pepper mode
    num_pepper = np.ceil(p* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    image_plus_noise[coords] = 0
    image_plus_noise = image_plus_noise.clip(0,255).astype(np.uint8)
    
    return image_plus_noise
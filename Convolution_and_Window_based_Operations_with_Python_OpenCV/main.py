import cv2
import load_image


for x in [1]:
    images=load_image.open_multiple_images(x)
    print(images)
    for img in images.values():
        cv2.imshow("Original",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()            

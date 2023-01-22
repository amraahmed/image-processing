import cv2

image = cv2.imread('galaxy.jpeg',0)



#Conver image to a grey scaled image

# cv2.imwrite("grey-scaled.jpeg",color)

#Resize Image

Osize = image.shape


def calculate_size(scale,w,h):
    W = int(w*scale/100)
    H =int(h*scale/100)
    return (W,H)



def resize(path,scale,resized_path):
    image = cv2.imread(path)
    new_dim = calculate_size(scale,image.shape[1],image.shape[0])
    resized_img = cv2.resize(image,new_dim)
    cv2.imwrite(resized_path,resized_img)


resize('img.png',500,'resizedimg.png')    




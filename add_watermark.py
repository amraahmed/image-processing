import cv2

image = cv2.imread('elfs.jpeg')
WM = cv2.imread('watermark.png')

x = image.shape[1] - WM.shape[1]
y = image.shape[0] - WM.shape[0]


WM_position = image[y:,x:]
cv2.imwrite('watermark_place.jpeg',WM_position)
blend = cv2.addWeighted(WM_position,.5,WM,.5,0)
cv2.imwrite('blend.jpeg',blend)


image[y:,x:] = blend
cv2.imwrite("watermarked.jpeg",image)
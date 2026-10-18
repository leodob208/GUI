import cv2
import numpy as np
image = cv2.imread('pika.png')
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('pika.png')


kernel= np.ones((5,5),np.uint8)
erosion = cv2.erode(image,kernel,iterations = 1)
cv2.imshow('Erosion image', erosion)

cv2.waitKey(0)

image = cv2.imread('pika.png')
bullerd= cv2.blur(image,(5,5))
cv2.imshow('Blurred image', bullerd)
cv2.waitKey(0)
cv2.destroyAllWindows()


image = cv2.imread('pika.png')
gussian= cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('Gussian image', gussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
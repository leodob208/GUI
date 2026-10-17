import cv2
import numpy as np

image = cv2.imread('/Users/leodobrov/Library/Application Support/zoom.us/data/confres/228f2982126ef1a810d14e57061a5301831e0798bcd3ef65442b0e8dc8be07fa/A3F1970F-D895-4A98-9628-CFCC41B6C764.png')
if image is None:
    print("Error: Could not read the image.")
    exit()

cv2.imshow('Original Image', image)
cv2.imwrite('original_image.png', image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)
cv2.imwrite('grayscale_image.png', gray_image)

blue,green,red = cv2.split(image)
cv2.imshow("Blue Channel", cv2.merge([blue, zeros, zeros]))

cv2.imshow('Green Channel', cv2.merge([np.zeros_like(green), green, np.zeros_like(green)])
           )

cv2.imshow('Red Channel', cv2.merge([np.zeros_like(red), np.zeros_like(red), red])
           )    

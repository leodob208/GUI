import cv2

image = cv2.imread('pika.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB Image', rgb_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

img = cv2.imread('pic.jpeg')

print('Original image size:', img.shape)

width = 500
height = 300

resized_img = cv2.resize(img, (width, height))

print('Resized image size:', resized_img.shape)


cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

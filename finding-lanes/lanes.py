import cv2
#import numpy as np

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)

cv2.imshow('Resultado', image)

cv2.waitKey(0)

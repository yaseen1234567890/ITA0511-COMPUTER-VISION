# import required libraries
import cv2
import numpy as np
# read the input image
img = cv2.imread("C:/Users/Mohammed Yaseen A/Downloads/COMPUTER VISION/12th exp.py")
# find the height and width of image
# width = number of columns, height = number of rows in image array
rows,cols,ch = img.shape
# define four points on input image
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
# define the corresponding four points on output image
pts2 = np.float32([[100,50],[300,0],[0,300],[300,300]])
# get the perspective transform matrix
M = cv2.getPerspectiveTransform(pts1,pts2)
# transform the image using perspective transform matrix
dst = cv2.warpPerspective(img,M,(cols, rows))
# display the transformed image
cv2.imshow('Transformed Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

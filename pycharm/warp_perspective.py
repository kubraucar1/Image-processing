import cv2 as cv
import numpy as np

img = cv.imread("img.png")
print(img.shape)
widht , height = 250,350
point1 = np.float32([[20,160],[220,120],[120,340],[250,300]])
point2 = np.float32([[0,0],[widht,0],[0,height],[widht,height]])

matrix = cv.getPerspectiveTransform(point1,point2)
imgOutput = cv.warpPerspective(img,matrix,(widht,height))

cv.imshow("image",img)
cv.imshow("output",imgOutput)
cv.waitKey(0)

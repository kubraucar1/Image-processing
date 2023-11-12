import cv2 as cv

img = cv.imread("girl.jpg")
print(img.shape)

imgResize = cv.resize(img,(400,300))
print(imgResize.shape)

#cv kullanarak resize yaparsak (widht,height)
#cropp işleminde olduğu gibi matris kullanırsak (height,widht) olarak yazılır

imgCropped = img[0:500,400:800]
cv.imshow("Image",img)
cv.imshow("Image resize",imgResize)
cv.imshow("Image Cropped",imgCropped)
cv.waitKey(0)

import cv2 as cv 


def color_space_demo(image):
    gray =cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HLS)
    cv.imshow("hsv",hsv)
    yuv=cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    Ycrvb =cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb",Ycrvb)

def cv_show(name,image):
    cv.imshow(str(name),image)
    cv.waitKey(0)
    cv.destroyWindow()
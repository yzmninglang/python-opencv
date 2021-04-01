import cv2 as cv 
import numpy as np


def video_demo():
    capture=cv.VideoCapture(0)
    while(True):
        ret,frame=capture.read()
        frame=cv.flip(frame,1)
        cv.imshow("video",frame)
        c=cv.waitKey(50)
        if c==27:
            break

def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data=np.array(image)
    print(pixel_data)


print("------------hello python------------")
src = cv.imread("./data1/1.png",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
get_image_info(src)
video_demo()
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imwrite('./data1/result1.jpg',gray)
cv.waitKey(0)


cv.destroyAllWindows()
import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height=image.shape[0]
    width=image.shape[1]
    channel=image.shape[2]
    print("height:%s width:%s channel:%s"%(height,width,channel))
    for i in range(height):
        for m in range(width):
            for k in range(channel):
                pv=image[i,m,k]  #Rgb of every pixel
                image[i,m,k]=255-pv
    cv.imshow("hello",image)

def inverse(image):
    dst=cv.bitwise_not(image)
    cv.imshow("inverse",dst)





def create_image():
    '''
    img=np.zeros([400,400,3],np.uint8)
    img[:,:,1]=np.ones([400,400])*255
    print(img[:,:,0])
    cv.imshow("heloo",img)
    '''
    # img=np.zeros([400,400,1],np.uint8)
    # # img[:,:,0]=np.ones([400,400])*127
    # img=img*127
    # print(img.shape[1])
    # cv.imshow("hello",img)
    # ml =np.ones([3,3],np.uint8)
    # ml.fill(212)
    # m2=ml.reshape([9,1])
    # print(m2)
    m3=np.array([[1,2,3],[4,5,6],[7,8,9]],np.int32)
    # m3.fill(9)
    print(m3)

print("----------Hello Python-----------")
src=cv.imread("./data1/1.png")
# create_image()
# cv.namedWindow("Are you ok?",cv.WINDOW_AUTOSIZE)
# cv.imshow("are you ok?",src)
t1=cv.getTickCount()   #get the function how much time it cost
# access_pixels(src)
create_image()
t2=cv.getTickCount()
time=1000*(t2-t1)/cv.getTickFrequency()
print("Time:%s"%time)
cv.waitKey(0)
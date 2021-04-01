import cv2 as cv 
import numpy as np 

def acess_pixels(image):
    print(image.shape)
    height=image.shape[0]
    width=image.shape[1]
    channels=image.shape[2]
    # print(type(channels))
    print("width : %s ,height: %s , channels: %s "%(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv=image[row,col,c]
                image[row,col,c] =255-pv
    cv.imshow("change image",image)

def create_image():
    '''
    img=np.zeros([400,400,3],np.uint8)
    img[:,:,1] =np.ones([400,400])*255
    img[:,:,0] =np.ones([400,400])*255
    # print(img.shape[2])
    print(img[:,:,2])
    cv.imshow("input image",img)
    '''
    # img=np.zeros([400,400,1],np.uint8)
    # img[:,:,0]=np.ones([400,400])*127
    # cv.imwrite("./data1/course2.png",img)
    # print(img.shape[2])
    # cv.imshow("new imge",img)
    ml=np.ones([400,400,2],np.float32)
    ml.fill(122.388)
    print(ml.shape[2])
    # ml[:,0]=np.ones([400,400])*126
    print(ml[:,0])
    # cv.imshow("1",ml)



print("-------hello python---------")
src=cv.imread("./data1/1.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
t1=cv.getTickCount()
create_image()
t2=cv.getTickCount()
print("Time : %s s"%((t2-t1)/cv.getTickFrequency()))
cv.waitKey(0)


cv.destroyAllWindow()
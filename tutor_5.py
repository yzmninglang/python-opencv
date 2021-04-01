import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt  


def cv_show(name,image):
    cv.imshow(name,image)
    cv.waitKey(0)
    cv.destroyWindow(name)


# for i,name in zip(images,title):
#     cv_show(name,i)

# for i in range(5):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(title[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()




#noise processed
src = cv.imread('./data2/Noise.png')
median=cv.medianBlur(src,5)
# median=cv.medianBlur(median,5)
res=np.hstack((src,median))
cv.imshow('res',res)
cv.waitKey(0)
cv.destroyAllWindows()
# cv.imshow('src',src)
# title=['src','median']
# images=[src,median]

# for i in range(2):
#     plt.subplot(1,2,i+1),plt.imshow(images[i])
#     plt.title(title[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
# cv.waitKey(0)
# cv.destroyAllWindows()

# blur=cv.blur(src,(3,3))
# for i in range(3):
#     blur=cv.blur(blur,(3,3))
# box=cv.boxFilter(src,-1,(3,3),normalize=False)
# aussian=cv.GaussianBlur(src,(9,9),1)
# aussian=cv.GaussianBlur(aussian,(7,7),1)
# aussian=cv.GaussianBlur(src,(5,5),1)
# aussian=cv.GaussianBlur(aussian,(3,3),1)
# title=['src','aussian']
# images=[src,aussian]
# for i in range(2):
#     plt.subplot(1,2,i+1),plt.imshow(images[i])
#     plt.title(title[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

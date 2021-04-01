import numpy as np 
import cv2 as cv 

img =cv.imread('./data2/ysu.png')
up = cv.pyrUp(img)
up_down = cv.pyrDown(up)
res=img-up_down







# img =cv.imread('./data2/Noise.png')
# up = cv.pyrUp(img)
# down= cv.pyrDown(up)
# res=np.hstack((img,down))




# img =cv.imread('./data2/ysu.png')
# up=cv.pyrUp(img)
# res=up
# print('up:',up.shape)
# print('img:',img.shape)















cv.imshow('img',res)
cv.waitKey(0)
cv.destroyAllWindows()
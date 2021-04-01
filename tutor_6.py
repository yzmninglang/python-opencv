import numpy as np 
import cv2 as cv 

# img = cv.imread('./data2/ysu.png')
# # print(img.shape)
# v1=cv.Canny(img,80,150)
# # res=np.hstack((img,v1))
# res = 255-v1


# img = cv.imread('./data2/2.jpg')
# v1=cv.Canny(img,120,250)
# v2=cv.Canny(img,50,100)
# res=np.hstack((v1,v2))







# img = cv.imread('./data2/Noise.png')
# v1 = cv.Canny(img,80,150)
# v2 = cv.Canny(img,50,100)
# res=np.hstack((v1,v2))


 










# res=img
# Sobelx=cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
# Sobelx=cv.convertScaleAbs(Sobelx)
# Sobely=cv.Sobel(img,cv.CV_64F,0,1,ksize=3)
# Sobely=cv.convertScaleAbs(Sobely)
# sobelxy=cv.addWeighted(Sobelx,0.5,Sobely,0.5,0)
# res=np.hstack((img,s obelxy))





# kernel=np.ones((5,5),np.int8)
# BLACKHAT=cv.morphologyEx(img,cv.MORPH_TOPHAT,kernel)
# res=np.hstack((img,BLACKHAT))







# kernel=np.ones((5,5),np.int8)
# gradient=cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)
# res=np.hstack((img,gradient))
# kernel=np.ones((5,5),np.int8)
# dilate=cv.dilate(img,kernel,iterations=1)
# erode=cv.erode(img,kernel,iterations=1)

# img2=dilate-erode
# res=np.hstack((img,img2))








# The close of opencv
# kernel=np.ones((5,5),np.int8)
# img3=cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
# res=np.hstack((img,img3))

# The open operation of opencv
# kernel=np.ones((5,5),np.int8)
# img3=cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
# res=np.hstack((img,img3))



# dilate in opencv
# kernel= np.ones((3,3),np.int8)
# img2=cv.dilate(img,kernel,iterations=1)
# res=np.hstack((img,img2))


# erode in opencv
# kernel = np.ones((2,1),np.int8)
# erosion= cv.erode(img ,kernel, iterations=10)
# res=np.hstack((img,erosion))
cv.imshow('img',res)
cv.waitKey(0)
cv.destroyAllWindows()
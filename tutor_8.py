import numpy as np
import cv2 as cv 














# img=cv.imread("./data2/5.jpg")
# res =img
# gary=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# ret,thresh=cv.threshold(gary,127,255,cv.THRESH_BINARY)
# binary, contours ,hierarchy =cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
# cnt =contours[0]





#circle
'''
(x,y),radius=cv.minEnclosingCircle(cnt)
center =(int(x),int(y))
radius=int(radius)
res=cv.circle(img,center,radius,(0,255,0),2)
'''




#rectangle of outbounding
'''
x,y,w,h=cv.boundingRect(cnt)
res=cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
epsilon = 0.01*cv.arcLength(cnt, True)  # Threshold of the dection
approx=cv.approxPolyDP(cnt,epsilon,True)
draw_img = img.copy()
# res = cv.drawContours(draw_img, [approx], -1, (0, 0, 255), 8)

'''



# img =cv.imread('./data2/Noise.png')
# gary =cv.cvtColor(img,cv.COLOR_BGR2GRAY)  #change the picture to gray 
# ret, thresh = cv.threshold(gary ,127,255,cv.THRESH_BINARY)   # make the picture to black and white (just two colors)
# # print(ret)
# res=thresh
# binary,contours,hierachy =cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)   #get the contours 
# # print(np.array(contours).shape)
#             #shape is the number of the Child element
# draw_img=img.copy()
# res=cv.drawContours(draw_img,contours,-1,(255,0,0),5)   #The fist parameter is the picture I want to deal ,the second
#             #is the contours you have got at the top, the  third is the number of 
            #contours you want to draw ,and the (255,0,0)is the rgb of the pencolor
            #the fourth parameter is the pensize 
# cnt=contours[78]
# print(cv.contourArea(cnt))   #the area of contours 
# print(cv.arcLength(cnt, True))  # the perimeter of contours

# res=gary
# cv.imshow("binary",binary)

# img = cv.imread("./data2/1.jpg")
# gary = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# ret, thresh =cv.threshold(gary,127,255,cv.THRESH_BINARY)
# binary,contours,hierachy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)


# cv.show(img,'img')
cv.imshow("res",res)
cv.waitKey(0)
cv.destroyAllWindows()









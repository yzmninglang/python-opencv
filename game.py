import cv2
import numpy as np
import turtle
 
def array_pic(pic):
    image = cv2.imread(pic,0)
    edges = cv2.Canny(image,80,130)
    img_gray = cv2.cvtColor(edges,cv2.COLOR_BAYER_BG2GRAY)
    ret, thresh = cv2.threshold(img_gray,127,255,0)
   
    image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    xy = []
    for i in range(0,len(contours)):
        x,y,w,h = cv2.boundingRect(contours[i])
        list_xy = [x,y]
        xy.append(list_xy)
    with open("./1.txt",'w') as f:
        for i in xy :
            f.write(str(i))
        f.close()
    return xy
    # file = open("array.txt", mode="x")
    # file.writelines(str(contours))
    # file.close()
    # cv2.imshow("1.jpg",image)
    # cv2.waitKey(0)
    
def draw(xy):
    # with open("./1.txt",'w') as f:
        # f.write(xy)
    
    turtle.pensize(2)
    turtle.setup(width=0.6,height=1.0)
    turtle.speed("fastest")
    for array in xy[::-1]:
        turtle.penup()
        turtle.goto((array[0])-600,-(array[1])+300)
        turtle.pendown()
        turtle.forward(1)
        # print(turtle.pos())
        
    
    turtle.done()
 
 
if __name__ == "__main__":
    pic = "./data2/ysu.png"
    xy = array_pic(pic)
    draw(xy)

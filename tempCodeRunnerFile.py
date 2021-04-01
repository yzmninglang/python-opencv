


img =cv.imread('./data2/ysu.png')
up = cv.pyrUp(img)
up_down = cv.pyrDown(up)
res=img-up_down



import cv2
import numpy as np

circles=cv2.imread("balls.png")
c=0

graycircles=cv2.cvtColor(circles,cv2.COLOR_BGR2GRAY)

img = cv2.medianBlur(graycircles,5)

dc=cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,dp=1, minDist=50, param1=50, param2=30, minRadius=10, maxRadius=100)
dc = np.uint16(np.around(dc))
for i in dc[0, :]:
    cv2.circle(circles,(i[0],i[1]),i[2],(0,255,0),2)
    print("Radius",i[2])
    c=c+1
print("Total Balls=",c)    
    
cv2.imshow('detected circles',circles)
cv2.waitKey(0)
cv2.destroyAllWindows()    
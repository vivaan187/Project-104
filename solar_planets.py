import cv2 

img = cv2.imread("solar-system.jpg")
#Sun
cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
#Mercury
cv2.putText(img,"Mercury",(100,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
#Venus
cv2.putText(img,"Venus",(200,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
#Earth
cv2.putText(img,"Earth",(300,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
#Mars
cv2.putText(img,"Mars",(400,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
#Jupiter
cv2.putText(img,"Jupiter",(600,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
#Saturn
cv2.putText(img,"Saturn",(800,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
#Uranus
cv2.putText(img,"Uranus",(1000,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
#Neptune
cv2.putText(img,"Neptune",(1100,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow("image",img)
cv2.waitKey(0)
import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
c=0
print("Press 'q' to exit")

while True:

    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #cv2.imshow('Macbook_Cam0', frame)
    cv2.imshow('GreyScaled_Macbook_Cam0', grey)
    
    timeF = 10
    
    if(c%timeF == 0): #save as jpg every 10 frame  
         cv2.imwrite('~/train_dir/me'+str(c) + '.jpg',frame) #save as jpg

    c+=1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

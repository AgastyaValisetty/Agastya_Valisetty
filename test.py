
import cv2 #now with smile!!/mouth!!


face_cascade = cv2.CascadeClassifier('C:\\Users\\Agast\\Downloads\\opencv\\sources\\data\\lbpcascade\\lbpcascade_frontalface_improved.xml') 


leye_cascade = cv2.CascadeClassifier('C:\\Users\\Agast\\Downloads\\opencv\\sources\\data\\haarcascades\\haarcascade_lefteye_2splits.xml') 
reye_cascade = cv2.CascadeClassifier('C:\\Users\\Agast\\Downloads\\opencv\\sources\\data\\haarcascades\\haarcascade_righteye_2splits.xml') 
smile_cascade = cv2.CascadeClassifier('C:\\Users\\Agast\\Downloads\\opencv\\sources\\data\\haarcascades\\haarcascade_smile.xml') 
# capture frames from a camera 
cap = cv2.VideoCapture(0) 


while 1: 

	
	ret, img = cap.read() 

	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

	
	#faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

	for (x,y,w,h) in faces: 
	
		cv2.rectangle(img,(x,y),(x+w,y+h),(24,237,8),1) 
		roi_gray = gray[y:y+h, x:x+w] 
		roi_color = img[y:y+h, x:x+w] 

		
		leye = leye_cascade.detectMultiScale(roi_gray) 


		for (ex,ey,ew,eh) in leye: 
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0, 132, 255),1) 

		smile = smile_cascade.detectMultiScale(roi_gray) 

		
		#for (ex,ey,ew,eh) in smile: 
			#cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1) 

		reye = reye_cascade.detectMultiScale(roi_gray) 

		
		for (ex,ey,ew,eh) in reye: 
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0, 132, 255),1) 	


	
	cv2.imshow('img',img) 

	# Wait for Esc key to stop 
	k = cv2.waitKey(30) & 0xff
	if k == 27: 
		break


cap.release() 

cv2.destroyAllWindows() ,
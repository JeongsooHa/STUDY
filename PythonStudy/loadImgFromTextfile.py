import cv2
import os
import sys

def readAndPrediction(filename):
	filePath = "/home/spc/Documents/AirSim/"
	imgTextPath = open(filePath+filename+"/OUTIMAGE.txt","r")
	imgPath = filePath+filename+"/images/"
	directionText = open(filePath+filename+"/DIRECTION.txt","w")	

	
	#while(True):
	
	#imgtext = read a line using imgTextPath
	imgtext = imgTextPath.readline().splitlines()[0]
	print(imgtext)
	
	#rawimg = load image using imgtext and imgPath
	print(imgPath+imgtext)
	rawimg = cv2.imread(imgPath+imgtext,3)	
	#print(rawimg)
	cv2.imshow(imgtext,rawimg)

	#direction = predict(rawimg)
	#direction = model.predict(rawimg)
	direction = 0.0001	
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	
	#direction.txt << direction
	directionText.write(str(direction)+"\n")		
	
	imgTextPath.close()	
	directionText.close()

if __name__ == "__main__":
	filename = sys.argv[1]
	readAndPrediction(filename) 

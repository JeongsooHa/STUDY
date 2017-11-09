import cv2
import os
import sys

def readAndPrediction(filename):
	filePath = "/home/spc/Documents/AirSim/"
	activatedPath = filePath+filename

	imgTextPath = open(activatedPath+"/OUTIMAGE.txt","r")
	directionText = open(activatedPath+"/DIRECTION.txt","w")
	imgPath = activatedPath+"/images/"
		
	
	for imgtext in imgTextPath:

		#imgtext = read a line using imgTextPath
		imgtext = imgtext.splitlines()[0]
		
		print(imgtext)
	
		#rawimg = load image using imgtext and imgPath
		#print(imgPath+imgtext)
		rawimg = cv2.imread(imgPath+imgtext,3)	
		#print(rawimg)
		#cv2.imshow(imgtext,rawimg)

		#direction = model.predict(rawimg)

		direction = imgtext + str(0.0001) #example	
		
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
	
		#Write direction to DIRECTION.txt
		directionText.write(str(direction)+"\n")


	imgTextPath.close()	
	directionText.close()

if __name__ == "__main__":
	filename = sys.argv[1]
	readAndPrediction(filename) 

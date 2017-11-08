import os
import sys
import re

def readAndDirection(filename):
    filePath = "/home/spc/Documents/AirSim/"
    imgTextPath = open(filePath+filename+"/OUTIMAGE.txt","w")
	path_dir = filePath+filename+"/images"
    
    #make a files list in directory 
	file_list = os.listdir(path_dir)

    #Sort string by number
	list_arr = [int(re.search(r"(\d+)",item).group(1)) for item in file_list]
	a1 = zip(file_list,list_arr)
	a1.sort(key=lambda item:item[1])
	a2, a3 = zip(*a1)

    for item in a2:
        imgTextPath.write(str(item)+"\n")
	imgTextPath.close()

if __name__ == "__main__":
	filename = sys.argv[1]
        readAndDirection(filename)


import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
image_info=[]

f = open("/Users/jeongsooha/20bn-datasets/folderNameList.txt","r")
folder_list = f.readline().split(", ")
print(len(folder_list))

folder_list = folder_list[:int(len(folder_list)/2)]

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        print (x,y)
        ix,iy = x,y
        image_info.append(x)
        image_info.append(y)
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),2)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),2)
        print (x,y)
        image_info.append(x)
        image_info.append(y)

qq = open("/Users/jeongsooha/20bn-datasets/final.txt","r")
finalIndex = qq.readline().split(" ")
print(finalIndex[0])

for filenumber in folder_list[int(finalIndex[0]):]:
    mypath = "/Users/jeongsooha/20bn-datasets/20bn-jester-v1/"+filenumber+"/"
    image_list = listdir(mypath)
    print(filenumber)
    image_list = sorted(image_list)
    print(image_list)
    
    for image in image_list:
        print(image)
        image_name = image.replace(".jpg","")
        img = cv2.imread(mypath+image, cv2.IMREAD_COLOR)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',draw_circle)

        while(1):
            cv2.imshow('image',img)
            k = cv2.waitKey(1) & 0xFF

            if k == 109:
                t = open("/Users/jeongsooha/20bn-datasets/final.txt", 'w')
                t.write(str(folder_list.index(filenumber))+" "+filenumber+" / "+image)
                t.close()
                exit()
            elif k == 27:
                image_info = ['-1','-1','-1','-1']
                break
            if len(image_info)>7:
                image_info = image_info[:4]
                break
        cv2.destroyAllWindows()

        print(image_info)

        f = open("/Users/jeongsooha/20bn-datasets/gt/"+filenumber+"_"+image_name+".txt", 'w')
        str1 = ' '.join(str(e) for e in image_info)
        f.write(str1)
        f.close()
        image_info = []
    
   
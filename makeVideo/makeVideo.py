import cv2
import os
import sys

image_folder = sys.argv[1]
#output = 'output.mp4'
arg = sys.argv[2]
output = sys.argv[3]+".mp4"

#Can't sort
#images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

images = []
for f in os.listdir(image_folder):
    if f.endswith(arg):
        images.append(f)
images.sort()

# Determine the width and height from the first image
image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(image_path)
cv2.imshow('video',frame)
height, width, channels = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

for image in images:

    image_path = os.path.join(image_folder, image)
    frame = cv2.imread(image_path)
    out.write(frame) # Write out frame to video
    
    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()

print("The output video is {}".format(output))

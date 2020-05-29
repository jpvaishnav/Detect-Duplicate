import cv2
import numpy as np
import os
import sys
from get_diff import compute

pathIn = './data/input/'
pathOut='./data/output/'
files = [f for f in os.listdir(pathIn)]
s=set()
for i in range(len(files)):
    img1=cv2.imread(pathIn+files[i],0)
    img1=cv2.resize(img1, (1050, 1610)) 
    for j in range(i+1,len(files)):
        img2=cv2.imread(pathIn+files[j],0)
        img2=cv2.resize(img2, (1050, 1610)) 
        rows,cols=img2.shape[:2]
        for angle in range(0,6):
            #getRotationMatrix2D creates a matrix needed for transformation. 
            # We want matrix for rotation w.r.t center to 45 degree without scaling. 
            mat=cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
            img3=cv2.warpAffine(img2, mat, (cols, rows))
            dif=compute(img1,img3)
            if(dif<10):
                print("Duplicate found of Image IDs "+ str(i)+" "+str(j))
                s.add(j)
                break
    
    
print("Total duplicates are : "+str(len(s)))
cnt=1
for i in range(len(files)):
    if i in s:
        continue
    else:
        img=cv2.imread(pathIn+files[i])
        cv2.imwrite(str(pathOut)+"out "+str(cnt)+".jpg",img)
        cv2.waitKey(0)
        cnt+=1
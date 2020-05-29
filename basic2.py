import cv2
import numpy as np
import os
import sys
from get_diff import compute
#from skimage.measure import structural_similarity as ssim
from skimage import measure
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
        similar=measure.compare_ssim(img1,img2)
        #print(str(similar))
        if(similar>0.9):
            print("Duplicate found of Image IDs "+ str(i)+" "+str(j))
            s.add(j)

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
import cv2
import numpy as np
def compute(img1,img2):
    #--- take the absolute difference of the images ---
    res = cv2.absdiff(img1, img2)
    #cv2.imshow("Difference_frame",res)
    #key=cv2.waitKey(0)
    #--- convert the result to integer type ---
    res = res.astype(np.uint8)

    #--- find percentage difference based on number of pixels that are not zero ---
    percentage = (np.count_nonzero(res) * 100)/ res.size
    #print("Difference percentage is "+str(percentage))
    return percentage
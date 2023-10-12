import numpy as np
import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread(
    r"C:\Users\LeonG\Documents\DevCode\Microchips\Udemy\Computer-Vision-with-Python\DATA\crossword.jpg", 0)

# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

ret, thresh1 = cv2.threshold(img1, 127, 255, cv2.THRESH_TRUNC) #param1 = imput image oaram 2 = threshold very value above 127 get turned to max , below to zero, param 3 max val

print(ret)
plt.imshow(thresh1,cmap="gray")
plt.show()















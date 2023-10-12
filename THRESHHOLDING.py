import numpy as np
import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread(
    r"C:\Users\LeonG\Documents\DevCode\Microchips\Udemy\Computer-Vision-with-Python\DATA\crossword.jpg", 0)

# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# param1 = imput image oaram 2 = threshold very value above 127 get turned to max , below to zero, param 3 max val
ret, th1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(
    img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

blended = cv2.addWeighted(src1=th1, alpha=0.6, src2=th2, beta=0.4, gamma=0)


def show_image(img):
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap="gray")
    plt.show()


show_image(blended)

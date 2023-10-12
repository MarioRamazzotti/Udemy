import numpy as np
import cv2
import matplotlib.pyplot as plt

############################## THRESHOLD-OPTIONS##########################################################
# THRESH_BINARY (int):
# Alle Pixelwerte, die über dem Schwellenwert liegen,
# werden auf den maximalen Wert (normalerweise 255) gesetzt,
# und alle Pixelwerte, die darunter liegen, werden auf den minimalen Wert
# (normalerweise 0) gesetzt.
# Dies erzeugt ein binäres Schwarz-Weiß-Bild.

# THRESH_BINARY_INV (int):
# Das ist das Gegenteil von THRESH_BINARY.
# Alle Pixelwerte über dem Schwellenwert werden auf den minimalen Wert
# gesetzt, und alle Pixelwerte darunter werden auf den maximalen Wert gesetzt.##

# THRESH_TRUNC (int):
# Alle Pixelwerte über dem Schwellenwert bleiben unverändert,
# während alle Pixelwerte darunter auf den Schwellenwert selbst gesetzt werden.

# THRESH_TOZERO (int):
# Alle Pixelwerte über dem Schwellenwert bleiben unverändert,
# während alle Pixelwerte darunter auf den minimalen Wert gesetzt werden.

# THRESH_TOZERO_INV (int):
# Das ist das Gegenteil von THRESH_TOZERO.
# Alle Pixelwerte über dem Schwellenwert werden auf den minimalen Wert gesetzt,
# während alle Pixelwerte darunter unverändert bleiben.

# THRESH_MASK (int):
# Dies ist keine Schwellenwertmethode,
# sondern ein Flag, das mit anderen Schwellenwertmethoden kombiniert werden kann,
# um einen speziellen Ausgabemodus zu aktivieren.

# THRESH_OTSU (int):
# Dies ist eine adaptive Schwellenwertmethode,
# bei der der Schwellenwert automatisch basierend auf der Bildhelligkeit berechnet wird.
# Sie eignet sich besonders für Bilder mit ungleichmäßiger Beleuchtung.

# THRESH_TRIANGLE (int):
# Dies ist eine adaptive Schwellenwertmethode,
# bei der der Schwellenwert basierend auf dem histogrammbasierten
# Dreieck-Algorithmus berechnet wird. Es ist eine weitere Methode für
# Bilder mit ungleichmäßiger Beleuchtung.
#########################################################################################################


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
plt.show()
plt.show()

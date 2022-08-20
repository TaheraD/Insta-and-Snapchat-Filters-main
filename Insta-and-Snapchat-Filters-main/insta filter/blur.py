import cv2
import matplotlib.pyplot as plt
im = cv2.imread(r'C:\Users\pc\Downloads\Insta-and-Snapchat-Filters-main\Insta-and-Snapchat-Filters-main\insta filter\house.jpeg')
#dst = cv2.GaussianBlur(im,(5,5),0)
dst = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('rotated',dst)
#plt.show()
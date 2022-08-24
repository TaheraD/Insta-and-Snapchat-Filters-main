import cv2
import matplotlib.pyplot as plt
im = cv2.imread(r'C:\Users\pc\Downloads\Insta-and-Snapchat-Filters-main\Insta-and-Snapchat-Filters-main\insta filter\house.jpeg')
dst = cv2.GaussianBlur(im,(5,5),cv2.BORDER_DEFAULT)
plt.imshow(dst)
plt.show()

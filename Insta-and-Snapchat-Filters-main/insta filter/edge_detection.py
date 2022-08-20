import cv2
import matplotlib.pyplot as plt
im = cv2.imread(r'C:\Users\pc\Downloads\Insta-and-Snapchat-Filters-main\Insta-and-Snapchat-Filters-main\insta filter\flower.jpeg')
edges = cv2.Canny(im,100,300)
plt.imshow(edges)
plt.show()
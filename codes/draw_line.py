import cv2
point1 = (500,500)
point2 = (800, 600)
point_start = (point1[0] *2 - point2[0],point1[1] * 2 -point2[1])
point_end = (point2[0] *2 - point1[0],point2[1] *2 - point1[1])

print(point_start)
print(point_end)
color_ = (255, 255, 0)

color = (0, 255, 255)
img = cv2.imread("/Users/Dong/Desktop/test1.jpeg", 1)


cv2.line(img, point_start, point_end, color, 5)
cv2.line(img, point1, point2, color_, 5)
cv2.imshow("img",img)
cv2.waitKey()
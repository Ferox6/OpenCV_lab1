import cv2
import imutils
import numpy as np

image1 = cv2.imread("C:\post.jpg")

(blue, green, red) = image1[100 ,50]
print(blue, green, red)

cutted_image = image1[350:550 ,150:600]

resized_image = cv2.resize(image1, (700, 300))

rotated_image = imutils.rotate(image1, 32)

blurred_image = cv2.GaussianBlur(image1, (11, 11), 90)

summing_image = np.hstack((blurred_image, image1))

drawing = np.zeros((800,1000, 4), np.uint8)
cv2.line(drawing, (100, 300), (800, 300),(96, 96, 96),3)
cv2.circle(drawing, (725, 475), 100, (153, 153, 0), 3)

square_points = np.array([[100, 400], [100, 700], [400, 700], [400, 400]])
triangle_points = np.array([[500, 400], [500, 700], [800, 700]])

cv2.polylines(drawing, np.int32([square_points]), 1, (0,0,105), 3)
cv2.polylines(drawing, np.int32([triangle_points]), 1, (76,153,0), 3)

text = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(drawing, "Costanella", (100,250), text, 5, (255,255,255), 2)

cv2.imshow("image1", image1)
cv2.waitKey()
cv2.imshow("image1", cutted_image)
cv2.waitKey()
cv2.imshow("image1", resized_image)
cv2.waitKey()
cv2.imshow("image1", rotated_image)
cv2.waitKey()
cv2.imshow("image1", summing_image)
cv2.waitKey()
cv2.imshow("image1", drawing)
cv2.waitKey()
cv2.destroyAllWindows()
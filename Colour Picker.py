import cv2
import numpy as np

def cross(x):
    pass

img = np.zeros((300, 400, 3), np.uint8)
cv2.namedWindow('Colour Picker')



cv2.createTrackbar('B', 'Colour Picker', 0, 255, cross)
cv2.createTrackbar('G', 'Colour Picker', 0, 255, cross)
cv2.createTrackbar('R', 'Colour Picker', 0, 255, cross)

while True:
    cv2.imshow('Colour Picker', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    b = cv2.getTrackbarPos('B', 'Colour Picker')
    g = cv2.getTrackbarPos('G', 'Colour Picker')
    r = cv2.getTrackbarPos('R', 'Colour Picker')

    img[:] = [b, g, r]

cv2.destroyAllWindows()

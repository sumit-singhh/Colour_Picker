import cv2
import numpy as np

def cross(x):   #does nothing
    pass

def rgb_to_hex(rgb):
    hex_val ='%02x%02x%02x' % rgb
    return hex_val

def rgb_to_cmyk(r,g,b):
    if (r == 0) and (g == 0) and (b == 0):
        return 0, 0, 0, cmyk_scale
    else:
        k = 1 - (max(r,g,b)/255)
        c = (1 - r/255 - k)/(1 - k)
        m = (1 - g/255 - k)/(1 - k)
        y = (1 - b/255 - k)/(1 - k)
        return round(c*cmyk_scale,0),round(m*cmyk_scale,0),round(y*cmyk_scale,0),round(k*cmyk_scale,0)

img = np.zeros((300, 400, 3), np.uint8) #creates a window of size 300x400 px
cv2.namedWindow('Colour Picker')


cv2.createTrackbar('B', 'Colour Picker', 0, 255, cross)
cv2.createTrackbar('G', 'Colour Picker', 0, 255, cross)
cv2.createTrackbar('R', 'Colour Picker', 0, 255, cross)

while True: #infinite loop
    b = cv2.getTrackbarPos('B', 'Colour Picker')
    g = cv2.getTrackbarPos('G', 'Colour Picker')
    r = cv2.getTrackbarPos('R', 'Colour Picker')
    
    cv2.putText(img, f"Hex Value: #{rgb_to_hex((r,g,b))}", (2,18), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0))
    cv2.putText(img, f" CMYK: {rgb_to_cmyk(r,g,b)}", (150,11), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0))
    cv2.imshow('Colour Picker', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):   #press 'q' to quit 
        break

    img[:] = [b, g, r]    #set current bgr values to img matrix
    img = cv2.rectangle(img, (0,0), (400,20), (240,240,240), -1)

cv2.destroyAllWindows()

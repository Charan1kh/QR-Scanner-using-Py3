#libraries
import cv2 
import numpy as np
from pyzbar.pyzbar import decode

#decoder
def decoder(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcode = decode(gray_img)

    #points
    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)
        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        cv2.putText(image, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        print("Link: " + barcodeData + " | Type: " + barcodeType)
        return True  # Return True to indicate a barcode was found

    return False  # Return False if no barcode was found

#videoStills
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if decoder(frame):
        break  # Break the loop if a QR code is found
    cv2.imshow('Image', frame)
    code = cv2.waitKey(18)
    if code == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 3 is width for 640 pixels
cap.set(4, 480)  # 4 is high for 480 pixels

camera = True
with open('Database/Product_List') as f:
    P_List = f.read().splitlines()

while camera:
    success, frame = cap.read()
    success, frame2 = cap.read()
    cv2.rectangle(frame, (240, 160), (400, 320), (255, 255, 255), 1)
    cv2.line(frame, (240, 160), (280, 160), (136, 177, 18), 9)  # the upper left position
    cv2.line(frame, (240, 160), (240, 200), (136, 177, 18), 9)
    cv2.line(frame, (360, 160), (400, 160), (136, 177, 18), 9)  # the upper right position
    cv2.line(frame, (400, 200), (400, 160), (136, 177, 18), 9)
    cv2.line(frame, (360, 320), (400, 320), (136, 177, 18), 9)  # the lower right position
    cv2.line(frame, (400, 280), (400, 320), (136, 177, 18), 9)
    cv2.line(frame, (240, 320), (280, 320), (136, 177, 18), 9)  # the lower left position
    cv2.line(frame, (240, 280), (240, 320), (136, 177, 18), 9)
    #cv2.putText(frame, 'Scan Area', (238, 176), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    for code in decode(frame):
        print(code.type)
        myData = code.data.decode('utf-8')
        print(myData)
        if myData in P_List:
            myOutput = 'Recognized'
            myColor = (136, 177, 18)

        else:
            myOutput = 'Unrecognized'
            myColor = (0, 0, 255)
        cv2.putText(frame, myOutput, (239, 150), cv2.FONT_HERSHEY_COMPLEX, 1, myColor, 2)
        # cap.release(myData)
        # cv2.destroyWindow()
    cv2.imshow('Barcode Scanner', frame)
    cv2.imshow('Screen', frame2)
    if cv2.waitKey(1) == ord('q'):
        break

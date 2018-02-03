import numpy as np
import cv2

cap = cv2.VideoCapture('D:/Filmler/gifted/deneme.mp4') #parantezin içine sadece 0 yazarsak laptop kamerasý açýlýr.

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #videoyu gri yaptýk.bu kod kaldýrýlýrsa normal rengine geri döner

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):   #q ya basýnca kapanacak video penceresi
        break

cap.release()
cv2.destroyAllWindows()

import numpy as np
import cv2

cap = cv2.VideoCapture('D:/Filmler/gifted/deneme.mp4') #parantezin i�ine sadece 0 yazarsak laptop kameras� a��l�r.

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #videoyu gri yapt�k.bu kod kald�r�l�rsa normal rengine geri d�ner

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):   #q ya bas�nca kapanacak video penceresi
        break

cap.release()
cv2.destroyAllWindows()

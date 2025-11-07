import cv2
#carica l`immagine
immagine = cv2.imread("immagine_originale.jpg")
#mostra immagine 
cv2.imshow("Immagine originale:",  immagine)
#---Filtro 1
immagine_bn = cv2.cvtColor(immagine, cv2.COLOR_BGR2GRAY)
cv2.imshow("Bianco o Nero", immagine_bn)
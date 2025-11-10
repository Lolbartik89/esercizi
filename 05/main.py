import cv2
#carica l`immagine
immagine = cv2.imread("immagine_originale.jpg")
#controlla sel l`immagine 
if immagine is None:
    print("Errore: impossibile aprire l`immagine!")
    exit()
#Mosta l`immagine originale 
cv2.imshow("Immagine originale", immagine)
cv2.waitKey(1000)#Mostra per 1 secondo 
#--Filtro 1: Conversione in bianco e nero
bianco_nero = cv2.cvtColor(immagine, cv2.COLOR_BRG2GRAY)
#--Filtro 2: Ridimensione dell`immagine 
altezza, larghezza = bianco_nero.shape
nuova_dimensione = (larghezza // 2, altezza // 2)
ridimensionata = cv2.resize(bianco_nero, nuova_dimensione)
#Mostra i risultati
cv2.imshow("Filtro 1 - Bianco e Nero", bianco_nero)
cv2.imshow("Filtro 2 - Ridimensionata", ridimensionata)
cv2.waitKey(2000)#Mostra per  2 secondi

# Salvataggio del risultato 
cv2.imwrite("output_bn.jpg", bianco_nero)
cv2.imwrite("output_ridotta.jpg", ridimensionata)
# Chiude tutte le finestre
cv2.destroyAlWindows()
print("Filtri applicati e immagini salvate con successo.")
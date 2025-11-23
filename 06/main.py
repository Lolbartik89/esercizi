from PIL import Image 
import numpy as np
def calcola_luminosita(path_immagine):
 #apriamo immagine 
 img = Image.open(path_immagine).convert("RGB")
 array_img = np.array(img)
 luminosita = np.mean(array_img)
 return luminosita
def classifica_immagine(path_immagine, soglia=100):
 luminosita = calcola_luminosita(path_immagine)
 if luminosita > soglia: 

    return f"Immagine Chiara (luminosita = {luminosita:.2f})"
 else:
    return f"Immagine Scura (luminosita = {luminosita:.2f})"
if __name__ == "__main__":
   percorso = "immagine.jpg"
   risultato = classifica_immagine(percorso)
   print(risultato)
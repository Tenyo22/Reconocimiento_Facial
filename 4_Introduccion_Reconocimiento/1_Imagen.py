import cv2

# Contornos -> Conjunto de puntos o coordenadas las cuales nos sirve para encerrar e identificar una area de interes
imagen = cv2.imread('4_Introduccion_Reconocimiento/contorno.jpg')

# Mostrar imagen
cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

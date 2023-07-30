import cv2

imagen = cv2.imread('4_Introduccion_Reconocimiento/contorno.jpg')

# Conversion a escala grises
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# threshold -> Umbral simple
_, umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)

# findContours -> Curva que une los puntos continuos a lo largo de un limite
contorno, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# drawContours -> Dibujar los contornos
cv2.drawContours(imagen, contorno, -1, (251, 60, 50), 3)

cv2.imshow('Imagen Original', imagen)
cv2.imshow('Escala Grises', grises)
cv2.imshow('Imagen con umbral', umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()
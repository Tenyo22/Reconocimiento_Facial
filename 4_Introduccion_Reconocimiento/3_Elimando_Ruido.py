import cv2
import numpy as np

# Valores impares
valueGauss = 1
valueKernel = 5

original = cv2.imread('./4_Introduccion_Reconocimiento/monedassoles.jpg')

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# Reduccion de ruido
# Gaussianblur -> Suavizado de imagen
gauss = cv2.GaussianBlur(gray, (valueGauss, valueGauss), 0)

# Canny
canny = cv2.Canny(gauss, 60, 100)

kernel = np.ones((valueKernel, valueKernel), np.uint8) # Trabajar con 8 bytes

# MorphologyEx -> Operaciones basadas en la forma de la imagen
cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

contornos, jerarquia = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('Monedas encontradas: {}'.format(len(contornos)))

# Dibujar los contornos en la imagen original
cv2.drawContours(original, contornos, -1, (251, 60, 50), 2)

# Mostrar resultado
# cv2.imshow('Imagen Grises', gray)
# cv2.imshow('Imagen Gauss', gauss)
# cv2.imshow('Imagen Canny', canny)
cv2.imshow('Imagen Morphology', cierre)
cv2.imshow('Imagen Original', original)
cv2.waitKey(0)
import cv2


# Leitura da imagem
img = cv2.imread('roboedu.png')

if img is None:
    raise FloatingPointError("Não foi possível carregar a imagem PNG")


# Conversão de escala para cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Desenho de triângulos coloridos em regiões fixas
# Cada retângulo é definido por (x1, y1) conto superior esquerdo e (x2, y2) canto inferior direito
rects = [
    ((50,  50),  (200, 200), (0,   0, 255)),  # Vermelho
    ((250, 50),  (400, 200), (0, 255,   0)),  # Verde
    ((50, 250),  (200, 400), (255,   0,   0)) # Azul
]


# Preparar uma cópia colorida da imagem em tons de cinza
output = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

for (pt1, pt2, color) in rects:
    cv2.rectangle(output, pt1, pt2, color, thickness=3)


# Resultado
cv2.imshow("Resultado", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
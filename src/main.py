import cv2

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Não foi possível acessar a câmera.")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        print("Falha ao capturar o frame.")
        break

    cv2.imshow('Video ao Vivo', frame)

    tecla = cv2.waitKey(1)
    if tecla == ord('s'):
        cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('frame_cinza.jpg', cinza)
        print("Frame salvo!")
    elif tecla == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

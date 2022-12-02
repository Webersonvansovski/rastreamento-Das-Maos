# pip install opencv-python
# pip install mediapipe

import cv2
import mediapipe as mp

# víncular a webcam ao python
webcam = cv2.VideoCapture(0) # cria a conexão com a webcam

# inicializando o mediapipe
reconhecimento_maos = mp.solutions.hands
desenhos_mp = mp.solutions.drawing_utils
maos = reconhecimento_maos.Hands()


if webcam.isOpened():
    # vou ler minha webcam (webcam.read()
    validacao, frame = webcam.read()
    # criar loop infinito para pegar vários frames
    while validacao:
        # pegar o próximo frame da tela
        validacao, frame = webcam.read()

        # converte BGR (padrão do opencv) para RGB (padrão mediapipe)
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # desenhaer a mão
        lista_maos = maos.process(frameRGB)
        if lista_maos.multi_hand_landmarks:
            for mao in lista_maos.multi_hand_landmarks:
                desenhos_mp.draw_landmarks(frame, mao, reconhecimento_maos.HAND_CONNECTIONS)

        # mostrar o frame da webcam que o python ta vendo
        cv2.imshow("Video da Webcam", frame)
        # mandar o pyrhon esperar um pouco
        tecla = cv2.waitKey(2)
        # mandar ele parar o código quando eu apertar a tecla ESC
        if tecla == 27:
            break


# reconhecer as mãos usando o mediapipe



# desligar a conexão com a webcam
webcam.release()


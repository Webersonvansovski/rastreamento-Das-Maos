# Rastreamento dos Movimentos das Mãos

## O que foi usado?
  - Python
  - Opencv -> fazer a conexão com a Webcam
  - MediaPipe ->  fazer o reconhecimento das mãos
  
## Passo a Passo:
  ### instalação das bibliotecas:
     - pip install opencv-python 
     - pip install mediapipe
     
  ### Importação:
     - import cv2
     - import mediapipe as mp
     
  ### lógica usada:
     - víncular a webcam ao python
     - inicializando o mediapipe
     - vou ler minha webcam (webcam.read())
     - criar loop infinito para pegar vários frames
     - pegar o próximo frame da tela
     - converte BGR (padrão do opencv) para RGB (padrão mediapipe)
     - desenhar a mão
     - mostrar o frame da webcam que o python ta vendo
     - mandar o python esperar um pouco
     - mandar ele parar o código quando eu apertar a tecla ESC
     - desligar a conexão com a webcam

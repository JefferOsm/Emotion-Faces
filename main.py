# Importamos las librerias
from deepface import DeepFace
import cv2
import mediapipe as mp

# Declaramos la deteccion de rostros (Usando MediaPipe)
detros = mp.solutions.face_detection
rostros = detros.FaceDetection(min_detection_confidence= 0.8, model_selection=0)
# Dibujo
dibujorostro = mp.solutions.drawing_utils

# Abrir Camara y capturar imagenes
cap = cv2.VideoCapture(0)

# Empezar captura y recorrido de fotogramas
while True:
    # Leemos los fotogramas
    ret, frame = cap.read()

    frame = cv2.resize(frame, (800, 600)) 
    # Leer imagen ilustrativa para datos
    img =cv2.imread("img.jpg")
    img = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    ani, ali, c = img.shape

    # Correccion de color y conversion a rgb
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesamos
    resrostros = rostros.process(rgb)

    # Deteccion
    if resrostros.detections is not None:
        # Registramos
        for rostro in resrostros.detections:
            # Extraemos informacion de ubicacion
            al, an, c = frame.shape
            box = rostro.location_data.relative_bounding_box
            xi, yi, w, h = int(box.xmin * an), int(box.ymin * al), int(box.width * an), int(box.height * al)
            xf, yf = xi + w, yi + h

            # Dibujar recuadro
            cv2.rectangle(frame, (xi, yi), (xf, yf), (255, 0, 0), 1)
            frame[10:ani + 10, 10:ali+10] = img

            # Obtener Datos
            info = DeepFace.analyze(rgb, actions=['age', 'gender', 'emotion'], enforce_detection= False)
            print(info)
            
            # Edad
            edad = info[0]['age']
            # Emociones
            emociones = info[0]['dominant_emotion']
            # Genero
            gen = info[0]['dominant_gender']

        
            # Mapear generos y emociones para traducirlos
            genero_dic= {
                'Man': 'Hombre',
                'Woman': 'Mujer'
            }

            # Mapeo de emociones
            emociones_dic = {
                'angry': 'Enojado',
                'disgust': 'Disgustado',
                'fear': 'Miedoso',
                'happy': 'Feliz',
                'sad': 'Triste',
                'surprise': 'Sorprendido',
                'neutral': 'Neutral'
            }

            # Traducción del género
            gen = genero_dic.get(gen, gen)

            # Traducción de emociones
            emociones = emociones_dic.get(emociones, emociones)

            # Mostramos info
            cv2.putText(frame, str(gen), (55, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
            cv2.putText(frame, str(edad), (65, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
            cv2.putText(frame, str(emociones), (65, 155), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    # Mostramos los fotogramas
    cv2.imshow(" Deteccion de Edad ", frame)

    # Leemos el teclado
    t = cv2.waitKey(2)
    if t == 27:
        break

cv2.destroyAllWindows()
cap.release()

# Emotion-Faces
## 1. Instalacion Entorno
- Instalar Anaconda y crear un entorno virtual usando Python version 3.11.5  
https://www.anaconda.com/download/  
- Crear entorno (una vez instalado anaconda, usar shell de VSCode o Anaconda Prompt) :  
  Usar `create conda --name  emotionFace python=3.11.5`
- Activar entorno:  
  Usar `conda activate emotionFace`

## 2. Instalacion de librerias en el entorno(en el entorno)
una vez activado el entorno instalamos las librerias:  
- Mediapipe(Para la deteccion de rostros):
  Usar `pip install mediapipe` o `conda install -c conda-forge mediapipe`    
  https://pypi.org/project/mediapipe/
- Deepface( Modelos usados):
  Usar `pip install deepface` o
  `conda install -c conda-forge deepface`  
  https://pypi.org/project/deepface/

## 3. Usar entorno en visual studio code
- Con el codigo abierto presionar ctr + shift + p
- Seleccionar interprene
- Buscar el entorno creado en conda y seleccionarlo
  

si no se tiene webcam para probar, modificar cap = cv2.VideoCapture("ruta de uno de los videos carpeta videotest")

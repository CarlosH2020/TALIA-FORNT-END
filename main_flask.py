from flask import Flask, render_template, Response
import cv2


# Configurações do Flask
app = Flask(__name__)
cap = cv2.VideoCapture(0)
#face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

def generate():
     # Executa enquanto a webcam está ativa
     while cap.isOpened():
          # Coletando o conteúdo capturado pela câmera
          # Frame é a imagem capturada em si
          # ret é só um boooleano
          ret, frame = cap.read()
          delay_repeticao = delay_repeticao + 1

          (flag, encodedImage) = cv2.imencode(".jpg", frame)
          if not flag:
               continue
          yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/video_feed")
def video_feed():
     return Response(generate(),
          mimetype = "multipart/x-mixed-replace; boundary=frame")

@app.route('/translation')
def update():
    while True:
          time.sleep(1)
          global translated_text
          return jsonify(content=translated_text)

if __name__ == "__main__":
     app.run(debug=False)

cap.release()
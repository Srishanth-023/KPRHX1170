from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO("KPRHX1170/best.pt")

@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/live')
def live_monitoring():
    return render_template("live.html")

@app.route('/crimerate')
def crimerate():
    return render_template("crimerate.html")

@app.route('/criminalrecords')
def criminalrecords():
    return render_template("criminalrecords.html")

@app.route('/vehiclerecords')
def vehiclerecords():
    return render_template("vehiclerecords.html")

@app.route('/')
def welcome():
    return render_template("welcome.html")



def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            results = model(frame)
            annotated_frame = results[0].plot()

            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/liveob')
def liveob():
    return render_template("liveob.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(debug=True)

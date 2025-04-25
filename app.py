from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
import face_recognition
import numpy as np
import os

app = Flask(__name__)
model = YOLO("KPRHX1170/best.pt")

# Load face encodings
if os.path.exists("face_encodings.npy") and os.path.exists("face_names.npy"):
    known_face_encodings = np.load("face_encodings.npy", allow_pickle=True)
    known_face_names = np.load("face_names.npy", allow_pickle=True)
else:
    print("⚠️ Face encodings not found! Run encode_faces.py first.")
    known_face_encodings = []
    known_face_names = []

# -----------------------------------
# ROUTES
# -----------------------------------

@app.route('/')
def welcome():
    return render_template("welcome.html")

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

@app.route('/liveob')
def liveob():
    return render_template("liveob.html")

@app.route('/face_recognition')
def face_recognition_page():
    return render_template("face_recognition.html")

# -----------------------------------
# YOLO Object Detection Stream
# -----------------------------------

def gen_yolo_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        results = model(frame)
        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed_yolo')
def video_feed_yolo():
    return Response(gen_yolo_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# -----------------------------------
# Face Recognition Stream
# -----------------------------------

def gen_face_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):
            name = "Unknown"
            matches = face_recognition.compare_faces(known_face_encodings, encoding)

            if True in matches:
                index = matches.index(True)
                name = known_face_names[index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed_face')
def video_feed_face():
    return Response(gen_face_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# -----------------------------------

if __name__ == '__main__':
    app.run(debug=True)

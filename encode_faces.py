import os
import face_recognition
import numpy as np
import cv2

dataset_dir = "dataset"
encodings = []
names = []

for file in os.listdir(dataset_dir):
    if file.lower().endswith(('.jpg', '.png', '.jpeg')):
        img_path = os.path.join(dataset_dir, file)
        image = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(image)

        if encoding:
            encodings.append(encoding[0])
            name = os.path.splitext(file)[0]
            names.append(name)
            print(f"[✔] Encoded {file}")
        else:
            print(f"[❌] No face found in {file}")

np.save("face_encodings.npy", encodings)
np.save("face_names.npy", names)

print("✅ All encodings saved successfully.")

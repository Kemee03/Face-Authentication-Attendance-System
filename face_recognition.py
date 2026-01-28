import cv2
import os
import csv
import numpy as np
from datetime import datetime

print("FACE RECOGNITION STARTED")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_dir = os.path.join(BASE_DIR, "dataset")
attendance_file = os.path.join(BASE_DIR, "attendance.csv")


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_map = {}
label_id = 0

if not os.path.exists(dataset_dir):
    print("Dataset not found")
    exit()

for person in os.listdir(dataset_dir):
    person_path = os.path.join(dataset_dir, person)
    if not os.path.isdir(person_path):
        continue

    try:
        uid, name = person.split("_", 1)
    except:
        continue

    label_map[label_id] = (uid, name)

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            faces.append(img)
            labels.append(label_id)

    label_id += 1

labels = np.array(labels, dtype=np.int32)
recognizer.train(faces, labels)

print(f"Recognizer trained on {len(label_map)} students")


def mark_attendance(uid, name):
    mode = os.environ.get("PUNCH_MODE")  # IN or OUT
    today = str(datetime.now().date())
    now_time = datetime.now().strftime("%H:%M:%S")

    if not os.path.exists(attendance_file):
        rows = [["S.No", "UID", "Name", "Date", "PunchIn", "PunchOut"]]
    else:
        with open(attendance_file, "r", newline="") as f:
            rows = list(csv.reader(f))

    
    if mode == "IN":
        for row in rows[1:]:
            if len(row) >= 6 and row[1] == uid and row[3] == today:
                return

        serials = [int(r[0]) for r in rows[1:] if len(r) >= 6 and r[0].isdigit()]
        serial_no = max(serials) + 1 if serials else 1
        rows.append([serial_no, uid, name, today, now_time, ""])

    
    elif mode == "OUT":
        for row in rows[1:]:
            if len(row) >= 6 and row[1] == uid and row[3] == today and row[5] == "":
                row[5] = now_time
                break

    with open(attendance_file, "w", newline="") as f:
        csv.writer(f).writerows(rows)


cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in detected_faces:
        face_img = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face_img)

        if confidence < 80:
            uid, name = label_map[label]
            mark_attendance(uid, name)

            cv2.putText(
                frame,
                f"{name} ({uid})",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )
        else:
            cv2.putText(
                frame,
                "Unknown",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()

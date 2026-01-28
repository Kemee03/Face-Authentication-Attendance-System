import cv2
import os

print("FACE REGISTRATION STARTED")


uid = input("Enter Student UID: ").strip()
name = input("Enter Student Name: ").strip()

if uid == "" or name == "":
    print("UID or Name cannot be empty")
    exit()

person_id = uid + "_" + name


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(BASE_DIR, "dataset", person_id)

os.makedirs(dataset_path, exist_ok=True)


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Camera not opening")
    exit()

count = 0
MAX_IMAGES = 15

print(f"Registering face for: {person_id}")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]

        if face_img.size != 0 and count < MAX_IMAGES:
            img_path = os.path.join(dataset_path, f"{count}.jpg")
            cv2.imwrite(img_path, face_img)
            count += 1

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Face Registration (ESC to exit)", frame)

    if cv2.waitKey(1) == 27 or count >= MAX_IMAGES:
        break

cam.release()
cv2.destroyAllWindows()

print(f"{count} images saved in dataset/{person_id}")

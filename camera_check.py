import cv2

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    print("Camera is not working")
    exit()

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read frame")
        break

    cv2.imshow("Camera Test - Press ESC to exit", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()

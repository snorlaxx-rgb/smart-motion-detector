import cv2
import datetime
import os

folder_name = "motion_images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 2000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(folder_name, f"snapshot_{timestamp}.jpg")
        cv2.imwrite(filename, frame1)

    cv2.imshow("Motion Detector", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()
    if not ret:
        break
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
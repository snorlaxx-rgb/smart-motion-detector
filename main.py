import cv2
import datetime
import os
import time

images_folder = "motion_images"
videos_folder = "motion_videos"
os.makedirs(images_folder, exist_ok=True)
os.makedirs(videos_folder, exist_ok=True)

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

last_record_time = 0

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False
    total_area = 0
    for contour in contours:
        if cv2.contourArea(contour) < 2000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        motion_detected = True
        total_area += cv2.contourArea(contour)

    intensity = None
    if total_area > 0:
        if total_area < 5000:
            intensity = "Low"
        elif total_area < 15000:
            intensity = "Medium"
        else:
            intensity = "High"
        cv2.putText(frame1, f"Motion Intensity: {intensity}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    if motion_detected and (time.time() - last_record_time > 10):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        snapshot_file = os.path.join(images_folder, f"snapshot_{timestamp}.jpg")
        cv2.imwrite(snapshot_file, frame1)

        if intensity in ["Medium", "High"]:
            video_file = os.path.join(videos_folder, f"video_{timestamp}.avi")
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(video_file, fourcc, 20.0, (frame1.shape[1], frame1.shape[0]))

            start_time = time.time()
            while time.time() - start_time < 10:
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)
                cv2.imshow("Recording...", frame)
                if cv2.waitKey(10) == 27:
                    break
            out.release()
        last_record_time = time.time()

    cv2.imshow("Motion Detector", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()
    if not ret:
        break
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
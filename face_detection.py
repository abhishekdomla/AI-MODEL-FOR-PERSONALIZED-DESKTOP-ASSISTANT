import cv2
import os
from cv2 import Algorithm
import time
# import servo

# Step 1: Preparing video capturing

# Using haarcascade Algorithm

cascPath = os.path.dirname(cv2.__file__) + \
    "/data/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)


def draw_faces(frames, faces, radius):
    for (x, y, w, h) in faces:
        if w > 100 and h > 100:
            # Step 4: - Drawing rectangle around the face
            cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

            circlex = int(x + w/2)
            circleY = int(y+h/2)

            cv2.circle(frames, (circlex, circleY), radius, (255, 0, 0), -1)

while True:  # Step 2: - Converting and assign parameter value
    # Capture frame-by-frame
    ret, frames = video_capture.read()

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # dimension for red lines
    # height = frames.shape[0]
    # width = frames.shape[1]

    # cv2.line(frames, (int(width/2), 0), (int(width/2), height), (0, 0, 255), 2)
    # cv2.line(frames, (0, int(height/2)),
    #          (width, int(height/2)), (0, 0, 255), 2)

    radius = 8
    # Step 3: -X-axis and Y-axis red lines.
    # Draw a rectangle around the faces
    # if len(faces) > 0:
        # print(faces[0])

    draw_faces(frames, faces, radius)

    # time.sleep(5)

    # Display the resulting frame
    cv2.imshow("Video", frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
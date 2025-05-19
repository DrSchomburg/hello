import cv2
import numpy as np
try:
    import face_recognition
except ImportError:
    raise SystemExit("face_recognition library is required. Install via pip install face_recognition")


def capture_known_face(camera_index=0):
    """Capture an image from the webcam as the known face."""
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError("Could not open camera")
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise RuntimeError("Failed to capture image")
    return frame


def encode_face(image):
    """Return facial encodings for the first face in the image."""
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    if not boxes:
        raise RuntimeError("No face detected")
    return face_recognition.face_encodings(rgb, boxes)[0]


def recognize_loop(known_encoding, camera_index=0, threshold=0.6):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError("Could not open camera")

    print("Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for box, encoding in zip(boxes, encodings):
            match = face_recognition.compare_faces([known_encoding], encoding, tolerance=1-threshold)
            top, right, bottom, left = box
            color = (0, 255, 0) if match[0] else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            text = "Recognized" if match[0] else "Unknown"
            cv2.putText(frame, text, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        cv2.imshow('FaceID', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    print("Capturing known face. Look at the camera...")
    known_image = capture_known_face()
    known_encoding = encode_face(known_image)
    print("Starting recognition loop.")
    recognize_loop(known_encoding)


if __name__ == "__main__":
    main()

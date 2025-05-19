# FaceID Example Application

This repository provides a simple Python script that demonstrates basic face recognition. It captures a reference frame from your webcam and then attempts to recognize that face in real time.

## Requirements

- Python 3.8+
- [OpenCV](https://pypi.org/project/opencv-python/) (`cv2`)
- [face_recognition](https://github.com/ageitgey/face_recognition)

The `face_recognition` package relies on `dlib`, which may require additional system dependencies on macOS (Xcode command line tools). On Apple Silicon (M1/M2), install Python via a universal installer (e.g., `pyenv`) and ensure you have the required build tools.

Install the dependencies listed in `requirements.txt`:

```
pip install -r requirements.txt
```

## Usage

1. Ensure your webcam is accessible.
2. Run the script:

```
python face_id_app.py
```

The program will capture a single frame as the known face. Afterwards it starts the recognition loop. A green rectangle and "Recognized" label indicates a match. Press `q` to quit.

## Notes

- This is *not* Apple's Face ID technology, but an example using open-source libraries.
- Performance may vary depending on hardware and camera quality.


# gesture-controlled-mouse

A computer vision project that controls the mouse cursor using hand gestures through a webcam.

## Features

* Move cursor using index finger
* Click gesture detection
* Scroll up gesture
* Scroll down gesture
* Smooth cursor movement
* Real-time hand tracking using MediaPipe

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy

## How It Works

The project uses MediaPipe Hand Tracking to detect hand landmarks from webcam input. Different finger distances are used as gestures:

* Thumb + Middle Finger → Mouse Click
* Thumb + Ring Finger → Scroll Up
* Thumb + Pinky Finger → Scroll Down

The index finger controls cursor movement.

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## Future Improvements

* Drag and drop gesture
* Multi-hand support
* Volume/Brightness control
* Gesture customization
* Better smoothing and stability
* Virtual keyboard integration

## Author

Ashutosh Kumar

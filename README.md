# Lane Maintenance System using Hough Transform and Canny Edge Detection in Python

This project implements a lane detection system in Python using OpenCV. The system processes real-time video feed, identifies lane lines on the road, and highlights them to assist in lane maintenance. This is achieved through edge detection (Canny) and line detection (Hough Transform) methods.

## Features

- Detects lane lines in real-time video.
- Focuses on a region of interest (ROI) to improve lane detection accuracy.
- Highlights detected lanes to provide visual feedback for lane maintenance.

## Prerequisites

To run this project, you need:

- Python 3.x
- OpenCV library
- Numpy library

Install the required libraries with:
```bash
pip install opencv-python numpy
```

## Code Explanation

### Functions
- **process_frame**: The main function that processes each frame for lane detection. It performs grayscale conversion, Gaussian blurring, Canny edge detection, and Hough Transform to detect lane lines.

### Main Code
1. **Camera Initialization**: Captures video from the camera.
2. **Grayscale and Gaussian Blurring**: Reduces noise in each frame.
3. **Canny Edge Detection**: Detects edges in the frame.
4. **Region of Interest (ROI)**: Focuses on the lower half of the frame where lane lines are more likely to be visible.
5. **Hough Transform**: Detects lines within the ROI and filters those that align with typical lane slopes.
6. **Lane Line Overlay**: Draws detected lanes in green and overlays them on the original frame.

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/lane-maintenance-hough-transform.git
    ```
2. Run the script:
    ```bash
    python lane_detection.py
    ```

3. Press **q** to exit the display window.


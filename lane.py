import cv2
import numpy as np

def process_frame(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Canny Edge Detection
    edges = cv2.Canny(blurred, 50, 150)
    
    # Define a region of interest (ROI) to focus on the road section
    height, width = edges.shape
    mask = np.zeros_like(edges)
    polygon = np.array([
        [(0, height), (width, height), (width, height // 2), (0, height // 2)]
    ])
    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)
    
    # Hough Transform to detect lines
    lines = cv2.HoughLinesP(
        cropped_edges,  # Input edge-detected image
        rho=1,          # Distance resolution in pixels
        theta=np.pi / 180,  # Angle resolution in radians
        threshold=50,    # Minimum number of votes to be considered a line
        minLineLength=100,  # Minimum length of a line (in pixels)
        maxLineGap=50     # Maximum allowed gap between points on the same line
    )
    
    # Draw the side lanes in green
    line_image = np.zeros_like(frame)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            slope = (y2 - y1) / (x2 - x1 + 0.01)  # Add small value to avoid division by zero
            # Assuming side lanes have a high slope (close to vertical)
            if 0.5 < abs(slope) < 2.5:  # Tune slope range as needed for your use case
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
    
    # Overlay lane lines on original frame
    lane_detected = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    return lane_detected

# Capture video from the camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Process the frame
    lane_frame = process_frame(frame)
    
    # Display the output
    cv2.imshow("Lane Detection", lane_frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

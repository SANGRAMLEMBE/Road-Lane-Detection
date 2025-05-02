import cv2
import numpy as np

# Define a function to detect lanes in a frame
def detect_lanes(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection to extract edges
    edges = cv2.Canny(blur, 50, 150)

    # Define a region of interest (ROI) polygon
    height = frame.shape[0]
    width = frame.shape[1]
    roi = np.array([[(0, height), (width/2, height/2+50), (width/2, height/2+50), (width, height)]], dtype=np.int32)

    # Apply a mask to extract the ROI
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, roi, 255)
    masked_edges = cv2.bitwise_and(edges, mask)

    # Apply Hough transform to detect lines
    lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 15, np.array([]), minLineLength=40, maxLineGap=20)

    # Draw the detected lines on the frame
    line_image = np.zeros_like(frame)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 10)

    # Combine the line image with the original frame
    result = cv2.addWeighted(frame, 0.8, line_image, 1, 0)

    return result

# Open the video capture device
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        break

    # Detect lanes in the frame
    result = detect_lanes(frame)

    # Show the result
    cv2.imshow('result', result)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()

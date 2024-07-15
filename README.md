## This mini-project demonstrates a simple barcode decoder using OpenCV, NumPy, and Pyzbar. The script captures video input from the webcam, processes each frame to detect and decode barcodes, and displays the results.

### Requirements
1. Python 3
2. OpenCV
3. NumPy
4. Pyzbar

```pip install opencv-python```
```pip install numpy```
```pip install pyzbar```

### Implementation
Decoder Function: Converts the image to grayscale and detects barcodes.
Display Results: Draws polygons around detected barcodes, displays the data and type of each barcode on the frame.
Video Capture: Continuously captures video frames from the webcam, processes each frame using the decoder function, and displays the processed frame.

### Conclusion
This project provides a basic implementation of real-time barcode detection and decoding. It can be extended to support additional features and handle different types of barcodes.
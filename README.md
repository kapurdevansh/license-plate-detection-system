# License Plate Detection System

## Overview
The License Plate Detection System is designed to detect and recognize license plates from images. The system consists of three main components: capturing images using a camera, detecting license plates in the images, and recognizing the characters on the detected license plates.

## Project Structure
- `camera.py`: Script to capture images using a camera.
- `detection.py`: Script to detect license plates in images and save the cropped license plate images.
- `recognition.py`: Script to recognize characters from the cropped license plate images using OCR (Optical Character Recognition).

## Setup
To set up the project, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/kapurdevansh/license-plate-detection-system.git
   cd license-plate-detection-system
2. **Install dependencies:**
Ensure you have Python and pip installed. Then, install the required packages such as OpenCV and pytesseract.

3. **Set up Tesseract:**
Download and install Tesseract OCR from here.
Make sure to update the path to the Tesseract executable in recognition.py:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

**Usage**
**Capturing Images**

To capture images using a camera, run:

python camera.py

This will display a live camera feed. Press 's' to capture a snapshot, which will be saved in the specified directory.
Detecting License Plates

To detect license plates in captured images, run:

python detection.py

This will process the images in the input directory, detect license plates, and save the cropped images in the output directory.
Recognizing Characters

To recognize characters from the cropped license plate images, run:

python recognition.py

This will process the cropped license plate images and output the recognized text.

**Data Overview**

The project uses images captured from a camera. The images are processed to detect and recognize license plates. The processed images are saved in the output directory, and the detected bounding boxes are saved in CSV files.
Input Data

    Captured images using camera.py.

**Output Data**

    Detected license plate images with bounding boxes drawn using detection.py.
    Recognized text from the license plates using recognition.py.

**Contributing**

Contributions are welcome! Please fork the repository and create a pull request with your changes.

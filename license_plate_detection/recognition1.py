# -*- coding: utf-8 -*-
# =============================================================================
# import cv2
# import pytesseract
# import os
# 
# # Set the path to the Tesseract executable (change this to your Tesseract installation path)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 
# 
# def segment_characters(image):
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 
#     # Apply adaptive thresholding
#    # _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
# 
#     # Find contours of characters
#     contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 
#     # Filter contours based on area to remove noise
#     min_area = 100
#     contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
# 
#     # Sort contours from left to right
#     contours = sorted(contours, key=lambda cnt: cv2.boundingRect(cnt)[0])
# 
#     # Extract bounding boxes of characters
#     character_boxes = [cv2.boundingRect(cnt) for cnt in contours]
# 
#     # Crop and segment characters
#     characters = []
#     for box in character_boxes:
#         x, y, w, h = box
#         character = gray[y:y+h, x:x+w]
#         characters.append(character)
# 
#     # Visualize the segmentation process
#     visualization = image.copy()
#     for box in character_boxes:
#         x, y, w, h = box
#         cv2.rectangle(visualization, (x, y), (x + w, y + h), (0, 255, 0), 2)
# 
#     cv2.imshow('Segmentation Visualization', visualization)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# 
#     return characters
# 
# 
# 
# def recognize_characters(image_path):
#     # Read the image
#     image = cv2.imread(image_path)
# 
#     # Segment characters
#     characters = segment_characters(image)
# 
#     # Perform character recognition using pytesseract
#     recognized_text = ''
#     for character in characters:
#         text = pytesseract.image_to_string(character, config='--oem 3 --psm 11 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
#         recognized_text += text.strip()
# 
#     print('License Plate:', recognized_text)
# 
# if __name__ == "__main__":
#     # Specify the directory containing the detected images
#     detected_images_directory = 'E:/IPBA/byop/license_plate_detection/output/'
# 
#     # List all files in the detected images directory
#     detected_images = os.listdir(detected_images_directory)
# 
#     for image_filename in detected_images:
#         # Check if the file is a detected image
#         if image_filename.endswith('_detected.jpg'):
#             # Construct the full path to the detected image
#             image_path = os.path.join(detected_images_directory, image_filename)
# 
#             # Recognize characters using OCR
#             recognize_characters(image_path)
# =============================================================================

# import cv2
# import pytesseract
# import os

# # Set the path to the Tesseract executable (change this to your Tesseract installation path)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def segment_characters(image):
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply Gaussian blur to reduce noise
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#     # Apply adaptive thresholding
#     _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#     # Find contours of characters
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Filter contours based on aspect ratio and area to remove noise
#     min_aspect_ratio = 0.2
#     max_aspect_ratio = 1.5
#     min_area = 50
#     contours = [cnt for cnt in contours if min_aspect_ratio < cv2.boundingRect(cnt)[2] / cv2.boundingRect(cnt)[3] < max_aspect_ratio
#                                               and cv2.contourArea(cnt) > min_area]

#     # Sort contours from left to right
#     contours = sorted(contours, key=lambda cnt: cv2.boundingRect(cnt)[0])

#     # Extract bounding boxes of characters
#     character_boxes = [cv2.boundingRect(cnt) for cnt in contours]

#     # Crop and segment characters
#     characters = []
#     for box in character_boxes:
#         x, y, w, h = box
#         character = gray[y:y+h, x:x+w]
#         characters.append(character)

#     # Visualize the segmentation process
#     visualization = image.copy()
#     for box in character_boxes:
#         x, y, w, h = box
#         cv2.rectangle(visualization, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     cv2.imshow('Segmentation Visualization', visualization)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#     return characters

# def recognize_characters(image_path):
#     # Read the image
#     image = cv2.imread(image_path)

#     # Segment characters
#     # characters = segment_characters(image)

#     # # Perform character recognition using pytesseract
#     # recognized_text = ''
#     # for character in characters:
#     #     text = pytesseract.image_to_string(character, config='--oem 3 --psm 6 -l eng -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
#     #     recognized_text += text.strip()
#     recognized_text=pytesseract.image_to_string(image)
#     print('License Plate:', recognized_text)

# if __name__ == "__main__":
#     # Specify the directory containing the detected images
#     detected_images_directory = 'E:/IPBA/byop/license_plate_detection/output/'

#     # List all files in the detected images directory
#     detected_images = os.listdir(detected_images_directory)

#     for image_filename in detected_images:
#         # Check if the file is a detected image
#         if image_filename.endswith('_detected.jpg'):
#             # Construct the full path to the detected image
#             image_path = os.path.join(detected_images_directory, image_filename)

#             # Recognize characters using OCR
#             recognize_characters(image_path)


# import cv2
# import pytesseract
# import os

# # Set the path to the Tesseract executable (change this to your Tesseract installation path)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def recognize_characters(license_plate_image_path):
#     # Read the license plate image
#     license_plate_image = cv2.imread(license_plate_image_path)

#     # Convert the license plate image to grayscale
#     gray_license_plate = cv2.cvtColor(license_plate_image, cv2.COLOR_BGR2GRAY)

#     # Perform character recognition using pytesseract
#     recognized_text = pytesseract.image_to_string(gray_license_plate, config='--oem 1 --psm 7 -l eng -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
#     print('License Plate:', recognized_text)

# if __name__ == "__main__":
#     # Specify the directory containing the cropped license plate images
#     cropped_images_directory = 'E:/IPBA/byop/license_plate_detection/output/'

#     # List all files in the cropped images directory
#     cropped_images = os.listdir(cropped_images_directory)

#     for image_filename in cropped_images:
#         # Check if the file is a cropped license plate image
#         if image_filename.endswith('_cropped.jpg'):
#             # Construct the full path to the cropped image
#             cropped_image_path = os.path.join(cropped_images_directory, image_filename)

#             # Recognize characters using OCR
#             recognize_characters(cropped_image_path)

import cv2
import pytesseract
import os

# Set the path to the Tesseract executable (change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_characters(license_plate_image_path):
    # Read the license plate image
    license_plate_image = cv2.imread(license_plate_image_path)

    # Convert the license plate image to grayscale
    gray_license_plate = cv2.cvtColor(license_plate_image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    # thresh_license_plate = cv2.adaptiveThreshold(gray_license_plate, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Perform character recognition using pytesseract
    recognized_text = pytesseract.image_to_string(gray_license_plate, config='--oem 3 --psm 7 -l eng -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    print('License Plate:', recognized_text)

if __name__ == "__main__":
    # Specify the directory containing the cropped license plate images
    cropped_images_directory = 'E:/IPBA/byop/license_plate_detection/output/'

    # List all files in the cropped images directory
    cropped_images = os.listdir(cropped_images_directory)

    for image_filename in cropped_images:
        # Check if the file is a cropped license plate image
        if image_filename.endswith('_cropped.jpg'):
            # Construct the full path to the cropped image
            cropped_image_path = os.path.join(cropped_images_directory, image_filename)

            # Recognize characters using OCR
            recognize_characters(cropped_image_path)






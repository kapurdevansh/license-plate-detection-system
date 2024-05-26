# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:10:40 2024

@author: devansh
"""
import cv2
import os
import csv

def detect_license_plate(image_path, output_directory):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply edge detection using Canny
    edges = cv2.Canny(blurred, 30, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours by area in descending order
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Find the largest contour (potential license plate)
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        if len(approx) == 4:
            license_plate = approx
            break

    # Draw bounding box around the detected license plate
    if 'license_plate' in locals():
        cv2.drawContours(image, [license_plate], -1, (0, 255, 0), 2)

        # Save the output image with the detected license plate
        filename = os.path.splitext(os.path.basename(image_path))[0]
        output_filename = filename + '_detected.jpg'
        output_image_path = os.path.join(output_directory, output_filename)

        # Save the image
        cv2.imwrite(output_image_path, image)

        # Save bounding box coordinates to CSV
        bbox_csv_path = os.path.join(output_directory, filename + '_bounding_boxes.csv')
        with open(bbox_csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['x', 'y', 'width', 'height'])
            x, y, w, h = cv2.boundingRect(license_plate)
            writer.writerow([x, y, w, h])

        # Crop and save the license plate image
        license_plate_image = gray[y:y+h, x:x+w]
        cropped_image_path = os.path.join(output_directory, filename + '_cropped.jpg')
        cv2.imwrite(cropped_image_path, license_plate_image)

        print("Detected license plate saved at:", output_image_path)
        print("Cropped license plate saved at:", cropped_image_path)
        return output_image_path, cropped_image_path
    else:
        print("License plate not found.")
        return None, None

if __name__ == "__main__":
    # Specify the directory containing the images
    input_directory = 'E:/IPBA/byop/license_plate_detection/input/'
    #input_directory = 'E:/IPBA/byop/license_plate_detection/license_plate_detection/output/drive-download-20240323T164347Z-001/'

    # Specify the directory to save detected license plates
    output_directory = 'E:/IPBA/byop/license_plate_detection/output/'

    # List all files in the input directory
    input_images = os.listdir(input_directory)

    for image_filename in input_images:
        # Construct the full path to the input image
        image_path = os.path.join(input_directory, image_filename)

        # Perform license plate detection
        detect_license_plate(image_path, output_directory)




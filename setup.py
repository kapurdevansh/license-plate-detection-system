# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='license_plate_detection',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'pytesseract',
        'imutils'
    ],
)

# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/182WSXPsMPwhhnefaxzE978-81uKAr0xU
"""

print("Hello")

!git clone https://github.com/itheaks/HackTech_Showcasing.git

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/HackTech_Showcasing

!pip install -e '.[dev]'

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/HackTech_Showcasing/ultralytics/yolo/v8/detect

from google.colab import drive
drive.mount('/content/drive')

!python predict.py model=yolov8n.pt source="/content/drive/MyDrive/Time Pass/sample.mp4"

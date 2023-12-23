# HackTech_Showcasing
Final project ready for speed estimation.

To run this project in your system here are the instructions, in case of google colab change runtime to GPU.

## Cloning my GitHub repo
!git clone https://github.com/itheaks/HackTech_Showcasing.git

## Lets move to our required Directory
%cd /content/HackTech_Final

## Installing the required directory
!pip install -e '.[dev]'

## As I have used yolov8 model so lets move to the required directory
%cd /content/HackTech_Final/ultralytics/yolo/v8/detect

## Our project is ready to test lets connect our google drive and import the videos.
from google.colab import drive
drive.mount('/content/drive')

## Define location of your video
!python predict.py model=yolov8n.pt source="/content/drive/MyDrive/Time Pass/sample.mp4"

If you want to compress videos you can

Here is some output sample

### Input Video

https://github.com/itheaks/HackTech_Final/assets/134759689/2de30bcd-9ec2-485d-95c2-1c7661bfb66f

### Output Video

https://github.com/itheaks/HackTech_Final/assets/134759689/03a4d4b0-d342-42c2-b904-ce4a3063aeb9

### In case of confusion feel free to watch this video "https://drive.google.com/file/d/1wrdo2-8FPs7jSXyGxvcFgjLTVLM3ivWy/view?usp=sharing"

### Project Documentaion is as "https://drive.google.com/file/d/1e0x0wGr1d_BEFdl4ZphLnVflqqOlWPE6/view?usp=sharing"

### Any sort of doubt or more info needed feel free to contact aksmlibts@gmail.com

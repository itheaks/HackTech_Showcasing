# HackTech_Final
Final project ready for speed estimation.

To run this project in your system here are the instructions, in case of google colab change runtime to GPU.

## Cloning my GitHub repo
!git clone https://github.com/itheaks/HackTech_Final.git

## Lets move to our required Directory
%cd /content/HackTech_Final

## Installing the required directory
!pip install -e '.[dev]'

## As I have used yolov8 model so lets move to the required directory
%cd /content/HackTech_Final/ultralytics/yolo/v8/detect

## Lets download our DeepSort pytorch File
!gdown "https://drive.google.com/uc?id=11ZSZcG-bcbueXZC3rN08CM0qqX3eiHxf&confirm=t"

## Unzipping deep_sort_pytorch.zip
!unzip 'deep_sort_pytorch.zip'

## Lets setup our main predict while where all the code of speed estimation is available
!gdown "https://drive.google.com/uc?id=1lhUkvbn2K_KZIE1EdxZ4n2q-Ztc08GMW"

## To test lets connect our google drive and import the videos.
from google.colab import drive
drive.mount('/content/drive')

## Define location of your video
!python predict.py model=yolov8n.pt source="/content/drive/MyDrive/Amit Kumar Singh Final Submission HackTech/Given Videos/scene1_01.mp4"

If you want to compress videos you can

Here is some output sample

### Input Video

https://github.com/itheaks/HackTech_Final/assets/134759689/2de30bcd-9ec2-485d-95c2-1c7661bfb66f

### Output Video

https://github.com/itheaks/HackTech_Final/assets/134759689/03a4d4b0-d342-42c2-b904-ce4a3063aeb9



# DaciaSandero

### detection file without GUI, yolo.py

## Requirements:

*Python 3

*Matplotlib

*OpenCV2

*Keras

*Numpy

*any python IDE (tested on Anaconda)

*weights file, can be found on https://pjreddie.com/media/files/yolov3.weights

## Installation

Prerequisites:

```pip install matplotlib```

```pip install numpy```

```pip install opencv-python```

```pip install keras```

To run, open an Anaconda command prompt and go to the directory containing yolo.py

Download the weights file to the same directory

Ideally have the image to detect in the same folder

```python yolo.py --weights yolov3.weights --image [your image name here]```

Please note this does not work with fish due to training problems and such the classes were not modified.


### Dataset

## Requirements:

*ffmpeg package

*Notepad++

## Installation:

Clone or download files at https://www.kaggle.com/aalborguniversity/brackish-dataset

```conda install -c anaconda ffmpeg```

## Separation of video files into frames

- Move frameExtractor.py to root directory

- Open Anaconda command prompt and change working directory to the root of the dataset one

```python frameExtractor.py --inputFolder [insert path to the folder containing videos]```

## For use on Darknet

- Move all images and COCO annotations into one directory

- Move createDummyYOLOAnnotations.py to root directory

- Open Anaconda command prompt and change working directory to the root of the dataset one

```python createDummyYOLOAnnotations.py --inputFolder [insert path to the folder containing videos]```

## Modifying train.txt file to include file paths

- Open file using Notepad++ (other file editors might work as well)

- In the search option, select Replace

- Tick regular expression at the bottom of the page

- In the Find What box, write the power symbol "^"

- In the Replace with box, put in the path relative from the darknet file to the image file

- Click replace all

### API & GUI
## Requirements: 
*Python 3

*Numpy

*Python 3 tkinter

*OpenCV

*TensorFlow
 
## Installing:
To use GUI, please install the package using below command in anaconda prompt 

```conda install -c anaconda tk```


To use API, please install below package using below command in anaconda prompt

```pip install keras```

```pip install opencv-python```

## Settings:
Run this in a terminal to load the weight and change the image source to your source 

```python yolo.py --weights yolov3.weights --image IMG_whatever.jpg```

## GUI:
This show the GUI using ui.py

![The Build](./API_GUI/ui.PNG?raw=true)

## Noted:
For test2.py,it is the implement of GUI.So you can use command to load weights and please change the source of image and path 

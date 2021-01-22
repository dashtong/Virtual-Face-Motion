import cv2
import numpy as np
import random

fps =  30
img_array = []
size = [1260, 720]

def setfps(f):
    global fps
    fps = f

def appendNodding(times):
    global fps
    global img_array
    global size
    for _ in range(times):
        for i in range(4,10):
            filename = "nodding/nodding{}.jpg".format(i)
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = [width,height]
            img_array.append(img)

        for i in range(9, -1, -1):
            filename = "nodding/nodding{}.jpg".format(i)
            img = cv2.imread(filename)
            height, width, layers = img.shape
            img_array.append(img)

        for i in range(5):
            filename = "nodding/nodding{}.jpg".format(i)
            img = cv2.imread(filename)
            height, width, layers = img.shape
            img_array.append(img)
    # return img_array

def appendBlink(times):
    global fps
    global img_array
    global size
    for _ in range(times):
        for i in range(5):
            filename = "blink/blink{}.jpg".format(i)
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = [width,height]
            img_array.append(img)

        for i in range(4, -1, -1):
            filename = "blink/blink{}.jpg".format(i)
            img = cv2.imread(filename)
            height, width, layers = img.shape
            img_array.append(img)

        for _ in range(random.randint(fps*3, fps*5)):   # Stay Still
            filename = "nodding/nodding0.jpg"
            img = cv2.imread(filename)
            height, width, layers = img.shape
            img_array.append(img)
    # return img_array

def appendStill(sec: int):
    global fps
    global img_array
    global size
    for _ in range(fps*sec):
        filename = "nodding/nodding0.jpg"
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = [width,height]
        img_array.append(img)
    # return img_array

def img2vid( title):
    global fps
    global img_array
    global size
    
    # If want to have a higher quality video, use cv2.VideoWriter_fourcc(*'mp4v') instead
    out = cv2.VideoWriter('{}_VirtualVideo.mp4'.format(title),cv2.VideoWriter_fourcc(*'avc1'), fps, tuple(size))
    for i in range(len(img_array)):
        out.write(img_array[i])

    out.release()

if __name__ == "__main__":
    setfps(23)
    for _ in range(1):
        appendBlink(2)
        appendNodding(2)
        appendStill(1)
        # img2video.appendBlink(2)

    img2vid("sdfs")
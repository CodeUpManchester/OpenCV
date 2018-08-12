import numpy as np
import cv2

def nothing(x):
    pass

def showEdges(image, minVal, maxVal):
    edges = cv2.Canny(image, minVal, maxVal)
    newFrame = cv2.bitwise_and(image, image, mask = edges)
    cv2.imshow('Processed Feed', newFrame)

def getTrackbarValues():
    minValue = cv2.getTrackbarPos('Min', 'Processed Feed')
    maxValue = cv2.getTrackbarPos('Max', 'Processed Feed')
    return [minValue, maxValue]

camera = cv2.VideoCapture(0)
canReadCamera, frame = camera.read()
 
if (not canReadCamera):
    frame = cv2.imread('/home/drew/Downloads/speak-science-logo.png',

                  cv2.IMREAD_UNCHANGED)
    cv2.imshow('Test Image', frame)
    showEdges(frame)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    showEdges(frame, 100, 200)
    cv2.createTrackbar('Min', 'Processed Feed', 0, 255, nothing)
    cv2.createTrackbar('Max', 'Processed Feed', 0, 255, nothing)
    
    while (True):
        cv2.imshow('Camera Feed', frame)
        trackbarValues = getTrackbarValues()
        showEdges(frame, trackbarValues[0], trackbarValues[1])

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        ret, frame = camera.read()

    cv2.destroyAllWindows()

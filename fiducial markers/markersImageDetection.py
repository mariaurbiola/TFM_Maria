import itertools
import cv2 as cv
from cv2 import aruco
import numpy as np
import os
import yaml
from yaml.loader import SafeLoader
print("version openCV", cv.__version__)
print("path openCV", cv.__path__)

#markerCorners = np.array([[],[]])
#x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
#markerIds = np.array
#rejectedCandidates = np.array([[],[]])

#inputImage = (cv.imread("markersToDetect.png"))
inputImage = (cv.imread(os.path.dirname(__file__) + "/marker.jpg"))
#cv.imshow("Markers", inputImage)
#outputImage = inputImage


dictionary = aruco.getPredefinedDictionary(cv.aruco.DICT_5X5_250); #predefined dictionary
arucoParams = aruco.DetectorParameters_create()
objPoints = (np.array([[0, 0, 1], [15, 0, 1], [15, 15, 1], [0, 15, 1]], np.int32)).astype('float32')
corners, ids, rejectedImgPoints = aruco.detectMarkers(inputImage, dictionary, parameters=arucoParams)
imgPoints = (np.array([corners[0][0][0],corners[0][0][1],corners[0][0][2],corners[0][0][3]], np.int32)).astype('float32')



print("imgPoints",imgPoints)

#print("rejected",rejectedImgPoints)
with open('/home/maria/Escritorio/TFM/TFM_MariaUrbiola/calibrate camera/calibration.yaml',"r") as f:
    loadeddict = yaml.load(f, Loader=SafeLoader)
cameraMatrix = loadeddict.get('camera_matrix')
distCoefs = loadeddict.get('dist_coeff')
cameraMatrix = np.array(cameraMatrix)
distCoeffs = np.array(distCoefs)
retval, rvec, tvec = cv.solvePnP(objPoints, imgPoints, cameraMatrix, distCoeffs)
print ("Rotation ", rvec, "Translation", tvec)
print("retval",retval)
distance = tvec[2][0]
print("distance from camera to marker", distance , "cm")

outputImage = aruco.drawDetectedMarkers(inputImage, corners, ids, (0,255,0))

cv.imshow("Detected markers", outputImage)
cv.waitKey(0)
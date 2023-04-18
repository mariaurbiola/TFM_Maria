import cv2 as cv
print(cv.__version__)

#Predefined dictionary
predefinedDictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_5X5_250)
id = 3
sidePixels = 200
borderBits = 1
markerImage = cv.aruco.generateImageMarker(predefinedDictionary, id, sidePixels, borderBits)

cv.imwrite("markerPredefined3.png", markerImage)


#Automatic dictionary
numberOfMarkers = 10
numberOfBits = 5
automaticDictionary = cv.aruco.extendDictionary(numberOfMarkers, numberOfBits)
markerImage = cv.aruco.generateImageMarker(automaticDictionary, id, sidePixels, borderBits)

cv.imwrite("markerAutomatic3.png", markerImage)

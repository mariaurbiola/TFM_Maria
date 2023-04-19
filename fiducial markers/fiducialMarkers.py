import cv2 as cv
print(cv.__version__)

#Predefined dictionary
predefinedDictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_5X5_250)
id = 3
sidePixels = 200
borderBits = 1
markerImage = cv.aruco.generateImageMarker(predefinedDictionary, id, sidePixels, borderBits)

cv.imwrite("markerPredefined"+str(id)+".png", markerImage)


#Automatic dictionary
numberOfMarkers = 10
numberOfBits = 5
for i in range(numberOfMarkers):
    automaticDictionary = cv.aruco.extendDictionary(numberOfMarkers, numberOfBits)
    markerImage = cv.aruco.generateImageMarker(automaticDictionary, i, sidePixels, borderBits)

    cv.imwrite("markerAutomatic"+str(i)+".png", markerImage)

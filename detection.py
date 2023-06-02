from webcamDetection import runWebcamDetection
from imageFileDetection import runImageFileDetection
import os
import cv2
print(cv2.__version__)
print(cv2.__path__)

def detection(detection_mode):
    if detection_mode == 'webcam':
        print('webcam')
        runWebcamDetection()
    elif detection_mode == 'imageFile':
        path_to_media_folder = os.path.dirname(__file__) + '/mmpose_photos/'
        media_name = path_to_media_folder + 'persons.jpg' #change this with the name of the file
        runImageFileDetection(media_name)
        print('imageFIle')
    elif detection_mode == 'videoFile':
        path_to_media_folder = os.path.dirname(__file__) + '/mmpose_videos/'
        media_name = path_to_media_folder + 'videoTry.webm' #change this with the name of the file
        runImageFileDetection(media_name)
        print('imageFIle')
    else:
        print('nada')
        
detection_mode = 'webcam'
#detection_mode = 'webcam'

detection(detection_mode)
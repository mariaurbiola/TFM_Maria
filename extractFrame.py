# Opens the Video file
import cv2
cap= cv2.VideoCapture('/home/maria/Escritorio/TFM/TFM_MariaUrbiola/videos/result_video1.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i == 60:
        cv2.imwrite('/home/maria/Escritorio/TFM/TFM_MariaUrbiola/frames/result_video1Frame'+str(i)+'.jpg',frame)
    if i == 150:
        cv2.imwrite('/home/maria/Escritorio/TFM/TFM_MariaUrbiola/frames/result_video1Frame'+str(i)+'.jpg',frame)
    if i == 240:
        cv2.imwrite('/home/maria/Escritorio/TFM/TFM_MariaUrbiola/frames/result_video1Frame'+str(i)+'.jpg',frame)
    if i == 330:
        cv2.imwrite('/home/maria/Escritorio/TFM/TFM_MariaUrbiola/frames/result_video1Frame'+str(i)+'.jpg',frame)
    i+=1
'''
cap.release()
cv2.destroyAllWindows()
cap= cv2.VideoCapture('/home/maria/Escritorio/TFM/TFM_MariaUrbiola/videos/video1.mp4')
i=0
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i == 60:
        cv2.imwrite('/home/maria/Escritorio/TFM/TFM_MariaUrbiola/frames/testVideo1Frame'+str(i)+'.jpg',frame)
    if i == 150:
        cv2.imwrite('/home/maria/Escritorio/TFM/TFM_MariaUrbiola/frames/testVideo1Frame'+str(i)+'.jpg',frame)
    if i == 240:
        cv2.imwrite('/home/maria/Escritorio/TFM/TFM_MariaUrbiola/frames/testVideo1Frame'+str(i)+'.jpg',frame)
    if i == 330:
        cv2.imwrite('/home/maria/Escritorio/TFM/TFM_MariaUrbiola/frames/testVideo1Frame'+str(i)+'.jpg',frame)
    i+=1
 '''
cap.release()
cv2.destroyAllWindows()
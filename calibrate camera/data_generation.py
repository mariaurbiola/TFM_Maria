import cv2
from pathlib import Path

camera = cv2.VideoCapture(0)

print('focus',camera.get(cv2.CAP_PROP_FOCUS))
camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
#camera.set(cv2.CAP_PROP_FOCUS, -3) #if used a normal camera and not a webcam, a focus value needs to be given and not changed

#print('focus',camera.get(cv2.CAP_PROP_FOCUS))
#print('width',camera.get(cv2.CAP_PROP_FRAME_WIDTH ))
#camera.set(cv2.CAP_PROP_FRAME_WIDTH, 960 )
#camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720 )
#print('width',camera.get(cv2.CAP_PROP_FRAME_HEIGHT ))


root = Path(__file__).parent.absolute()
path = root.joinpath("calibrationImages")
#print("PATH", path)

count = 0
while True:
    name = str(path) + "/" + str(count)+".jpg"
    ret, img = camera.read()
    cv2.imshow("img", img)

    if cv2.waitKey(20) & 0xFF == ord('c'):
        cv2.imwrite(name, img)
        cv2.imshow("img", img)
        count += 1
        if cv2.waitKey(0) & 0xFF == ord('q'):

            break;
